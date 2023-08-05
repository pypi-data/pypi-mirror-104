import os
import glob
import numpy as np
import pandas as pd
from itertools import chain
from astropy.io import ascii
import multiprocessing as mp
from astropy.stats import mad_std

from pysyd.plots import set_plot_params
from pysyd.functions import *
from pysyd.models import *



def get_info(args):
    """Loads todo.txt, sets up file paths, loads in any available star information,
       and sets up matplotlib params.

    Parameters
    ----------
    args : argparse.Namespace
        command line arguments
    star_info : str
        the file path to the star_info.csv file containing star information. Default value is `'info/star_info.csv'`
    params : dict
        the pipeline parameters, which is saved to args.params

    Returns
    -------
    args : argparse.Namespace
        the updated command line arguments
    """

    params={}
    # Open star list
    if args.stars is None:
        with open(args.todo, "r") as f:
            args.stars = [int(float(line.strip().split()[0])) for line in f.readlines()]
    check_inputs(args)
    params['inpdir'] = args.inpdir
    params['outdir'] = args.outdir
    if args.parallel:
        todo = np.array(args.stars)
        args.verbose = False
        args.show = False
        if args.n_threads == 0:
            args.n_threads = mp.cpu_count()
        if len(todo) < args.n_threads:
            args.n_threads = len(todo)
        # divide stars into groups set by number of cpus/nthreads available
        digitized = np.digitize(np.arange(len(todo))%args.n_threads,np.arange(args.n_threads))
        groups = np.array([todo[digitized == i] for i in range(1, args.n_threads+1)], dtype=object)
    else:
        groups = np.array([])

    # Adding constants and the star list
    params.update({
        'numax_sun':3090.0, 'width_sun':1300.0, 'stars':args.stars, 'G':6.67428e-8, 'ofactor':args.ofactor,
        'show':args.show, 'oversample':args.ocorr, 'tau_sun':[5.2e6,1.8e5,1.7e4,2.5e3,280.0,80.0], 
        'tau_sun_single': [3.8e6, 2.5e5, 1.5e5, 1.0e5, 230., 70.], 'radius_sun': 6.95508e10, 'save':args.save, 
        'teff_sun':5777.0, 'mass_sun':1.9891e33, 'dnu_sun':135.1, 'keplercorr': args.keplercorr, 'groups':groups, 
    })
    # Set file paths
    for star in args.stars:
        params[star] = {}
        params[star]['path'] = '%s/%d/' % (args.outdir,star)
    args.params = params

    # Initialise parameters for the find excess routine
    args = get_excess_params(args)
    # Initialise parameters for the fit background routine
    args = get_background_params(args)
    # Get star info
    args = get_star_info(args)
    set_plot_params()

    return args


def check_inputs(args):
    """ Make sure the command line inputs are proper lengths based on the specified stars.

    Parameters
    ----------
    args : argparse.Namespace
        the command line arguments
    """

    checks={'lower_b':args.lower_b,'upper_b':args.upper_b,'lower_x':args.lower_x,
            'upper_x':args.upper_x,'dnu':args.dnu,'numax':args.numax}
    for check in checks:
        if checks[check] is not None:
            assert len(args.star) == len(checks[check]), "The number of values provided for %s does not equal the number of stars"%check


def get_excess_params(args):
    """Get the parameters for the find excess routine.

    Parameters
    ----------
    args : argparse.Namespace
        the command line arguments
    findex : dict
        the parameters of the find excess routine
    step : float
        TODO: Write description. Default value is `0.25`.
    binning : float
        logarithmic binning width. Default value is `0.005`.
    n_trials : int
        the number of trials. Default value is `3`.
    lower : float
        the lower frequency bound. Default value is `10.0`.
    upper : float
        the upper frequency bound. Default value is `4000.0`.

    Returns
    -------
    args : argparse.Namespace
        the updated command line arguments
    """

    findex = {
        'step': args.step,
        'binning': args.binning,
        'smooth_width': args.smooth_width,
        'lower_x': 10.,
        'upper_x': 5000.,
        'n_trials': args.n_trials,
    }

    # Initialise save folders
    if args.save:
        for star in args.params['stars']:
            if not os.path.exists(args.params[star]['path']):
                os.makedirs(args.params[star]['path'])
    args.findex = findex
    args.findex['results'] = {}

    return args


def get_background_params(args, box_filter=2.5, mc_iter=1, ind_width=50, n_rms=20, n_peaks=5, 
                          smooth_ps=1, slope=False, samples=False, clip_ech=True, clip_value=None, 
                          smooth_ech=None, interp_ech=False):
    """
    Get the parameters for the background-fitting routine.

    Parameters
    ----------
    args : argparse.Namespace
        the command line arguments

    Uses
    ----
    fitbg : dict
        the parameters relevant for the fit background routine, which is saved to args.fitbg
    box_filter : args.box_filter
        the size of the 1D box smoothing filter (in $\mu$Hz). Default value is `2.5`.
    ind_width : int
        the independent average smoothing width. Default value is `50`.
    n_rms : int
        number of data points to estimate red noise contributions. Default value is `20`.
    n_peaks : int
        the number of peaks to select. Default value is `10`.
    force : float
        if not false (i.e. non-zero) will force dnu to be the equal to this value. 
    clip : bool
        if true will set the minimum frequency value of the echelle plot to `clip_value`. Default value is `True`.
    clip_value : float
        the minimum frequency of the echelle plot. Default value is `0.0`.
    smooth_ech : float
        option to smooth the output of the echelle plot
    smooth_ps : float
        TODO: Write description. Default value is `1.0`.
    lower : Optional[float]
        the lower frequency bound. Default value is `None`.
    upper : Optional[float]
        the upper frequency bound. Default value is `None`.
    slope : bool
        if true will correct for edge effects and residual slope in Gaussian fit. Default value is `False`.
    samples : bool
        if true, will save the monte carlo samples to a csv. Default value is `True`.

    Returns
    -------
    args : argparse.Namespace
        the updated command line arguments
    """

    fitbg = {
        'box_filter': args.box_filter,
        'mc_iter': args.mc_iter,
        'ind_width': args.ind_width,
        'n_rms': args.n_rms,
        'n_peaks': args.n_peaks,
        'smooth_ps': args.smooth_ps,
        'slope': args.slope,
        'samples': args.samples,
        'clip_ech': args.clip_ech,
        'clip_value': args.clip_value,
        'smooth_ech': args.smooth_ech,
        'interp_ech': args.interp_ech,
    }

    # Harvey components
    fitbg['functions'] = {1: harvey_one, 2: harvey_two, 3: harvey_three, 4: harvey_four, 5: harvey_five, 6: harvey_six}

    # Initialise save folders
    if args.save:
        for star in args.params['stars']:
            if not os.path.exists(args.params[star]['path']):
                os.makedirs(args.params[star]['path'])
    args.fitbg = fitbg
    args.fitbg['results'] = {}
    args.fitbg['acf_mask'] = {}

    return args


def get_star_info(args, cols=['rad','logg','teff','numax','lower_x','upper_x','lower_b','upper_b','seed']):
    """
    Get star information stored in args.info. Please note: this is not required for pySYD to run
    successfully. Default value is `info/star_info.csv`.

    Parameters
    ----------
    args : argparse.Namespace
        the command line arguments
    cols : list
        the list of columns to provide stellar information for

    Returns
    -------
    args : argparse.Namespace
        the updated command line arguments
    """

    # Open file if it exists
    if os.path.exists(args.info):
        df = pd.read_csv(args.info)
        stars = df.stars.values.tolist()
        for i, star in enumerate(args.params['stars']):
            args.params[star]['excess'] = args.excess
            args.params[star]['background'] = args.background
            args.params[star]['force'] = False
            if star in stars:
                idx = stars.index(star)
                # Update information from columns
                for col in cols:
                    if not np.isnan(float(df.loc[idx,col])):
                        args.params[star][col] = float(df.loc[idx, col])
                    else:
                        args.params[star][col] = None
                # Add estimate of numax if the column exists
                if args.params[star]['numax'] is not None:
                    args.params[star]['dnu'] = 0.22*(args.params[star]['numax']**0.797)
                # Otherwise estimate using other stellar parameters
                else:
                    if args.params[star]['rad'] is not None and args.params[star]['logg'] is not None:
                        args.params[star]['mass'] = ((((args.params[star]['rad']*args.params['radius_sun'])**(2.0))*10**(args.params[star]['logg'])/args.params['G'])/args.params['mass_sun'])
                        args.params[star]['numax'] = args.params['numax_sun']*args.params[star]['mass']*(args.params[star]['rad']**(-2.0))*((args.params[star]['teff']/args.params['teff_sun'])**(-0.5))
                        args.params[star]['dnu'] = args.params['dnu_sun']*(args.params[star]['mass']**(0.5))*(args.params[star]['rad']**(-1.5))
            override={'lower_b':args.lower_b,'upper_b':args.upper_b,'lower_x':args.lower_x,
                      'upper_x':args.upper_x,'dnu':args.dnu,'numax':args.numax}
            for each in override:
                if override[each] is not None:
                    # if numax is provided via CLI, findex is skipped
                    if each == 'numax':
                        args.params[star]['excess'] = False
                        args.params[star]['numax'] = override[each][i]
                        args.params[star]['dnu'] = 0.22*(args.params[star]['numax']**0.797)
                    # if dnu is provided via CLI, this value is used instead of the derived dnu
                    elif each == 'dnu':
                        args.params[star]['force'] = True
                        args.params[star]['guess'] = override[each][i]
                    else:
                        args.params[star][each] = override[each][i]
                
    return args


def load_data(star):
    """
    Loads both the light curve and power spectrum data in for a given star,
    which will return `False` if unsuccessful and therefore, not run the rest
    of the pipeline.

    Parameters
    ----------
    star : target.Target
        the pySYD pipeline object

    Returns
    -------
    star : target.Target
        the pySYD pipeline object
    lc_data : bool
        will return `True` if the light curve data was loaded in properly otherwise `False`
    ps_data : bool
        will return `True` if the power spectrum file was successfully loaded otherwise `False`
    """

    star.ts = False
    star.ps = False
    star.note = ''
    # Now done at beginning to make sure it only does this one per star
    if glob.glob('%s/%d_*'%(star.params['inpdir'],star.name)) != []:
        star.note += '\n-------------------------------------------------\nTarget: %d\n-------------------------------------------------'%star.name

        # Load light curve
        if not os.path.exists('%s/%d_LC.txt' % (star.params['inpdir'], star.name)):
            star.note += '\n# WARNING: no time series data provided for %d'%star.name
        else:
            star.ts = True
            star.time, star.flux = get_file('%s/%d_LC.txt' % (star.params['inpdir'], star.name))
            star.cadence = int(np.nanmedian(np.diff(star.time)*24.0*60.0*60.0))
            star.nyquist = 10**6/(2.0*star.cadence)
            star.note += '\n# LIGHT CURVE: %d lines of data read'%len(star.time)

        # Load power spectrum
        if not os.path.exists('%s/%d_PS.txt' % (star.params['inpdir'], star.name)):
            star.note += '\n# ERROR: %s/%d_PS.txt not found' % (star.params['inpdir'], star.name)
        else:
            star.ps = True
            star.oversample = star.params['oversample']
            star.ofactor = star.params['ofactor']
            star.frequency, star.power = get_file('%s/%d_PS.txt' % (star.params['inpdir'], star.name))
            if star.params['keplercorr']:
                star = remove_artefact(star)
            star.note += '\n# POWER SPECTRUM: %d lines of data read' % len(star.frequency)

        # Only run if power spectrum is provided
        if star.ps:
            if star.ts:
                ofactor = int(round((1./((max(star.time)-min(star.time))*0.0864))/(star.frequency[1]-star.frequency[0])))
            else:
                ofactor = 1

            print(ofactor, star.ofactor)
            # Correct power spectrum for oversampling
            if star.oversample:
                if star.ofactor == 1:
                    if ofactor == star.ofactor and not star.ts:
                        star.note += '\n# No time series data and no oversampling factor provided'
                        star.note += '\n# Assuming the power spectrum is critically sampled'
                    elif ofactor == star.ofactor and star.ts:
                        star.note += '\n# The power spectrum is critically sampled'
                    else:
                        star.ofactor = ofactor
                        star.note += '\n# Oversampled by a factor of %d'%star.ofactor
                else:
                    if ofactor == star.ofactor:
                        star.note += '\n# Oversampled by a factor of %d'%star.ofactor
                    else:
                        star.note += '\n# WARNING:\n# oversampling factor provided != that calculated from the time series'
                # Create critically sampled PS
                star.freq = np.copy(star.frequency)
                star.pow = np.copy(star.power)
                star.resolution = (star.frequency[1]-star.frequency[0])*star.ofactor
                star.frequency = np.array(star.frequency[star.ofactor-1::star.ofactor])
                star.power = np.array(star.power[star.ofactor-1::star.ofactor])

            else:
                star.note += '\n# No oversampling correction'
                # Create critically sampled PS
                star.freq = np.copy(star.frequency)
                star.pow = np.copy(star.power)
                star.resolution = star.frequency[1]-star.frequency[0]
                star.frequency = np.copy(star.frequency)
                star.power = np.copy(star.power)
                    
            star.note += '\n# Time series cadence: %d seconds' % star.cadence
            star.note += '\n# Power spectrum resolution: %.6f muHz' % star.resolution

            # If running the first module, mask out any unwanted frequency regions
            if star.params[star.name]['excess']:
                # Make a mask using the given frequency bounds for the find excess routine
                mask = np.ones_like(star.freq, dtype=bool)
                if star.params[star.name]['lower_x'] is not None:
                    mask *= np.ma.getmask(np.ma.masked_greater_equal(star.freq, star.params[star.name]['lower_x']))
                else:
                    mask *= np.ma.getmask(np.ma.masked_greater_equal(star.freq, star.findex['lower_x']))
                if star.params[star.name]['upper_x'] is not None:
                    mask *= np.ma.getmask(np.ma.masked_less_equal(star.freq, star.params[star.name]['upper_x']))
                else:
                    mask *= np.ma.getmask(np.ma.masked_less_equal(star.freq, star.findex['upper_x']))
                star.freq = star.freq[mask]
                star.pow = star.pow[mask]
                if star.params[star.name]['numax'] is not None:
                    if star.params[star.name]['numax'] <= 500.:
                        star.boxes = np.logspace(np.log10(0.5), np.log10(25.), star.findex['n_trials'])*1.
                    else:
                        star.boxes = np.logspace(np.log10(50.), np.log10(500.), star.findex['n_trials'])*1.
        if star.verbose:
            print(star.note)
    return star


def get_file(path):
    """Load either a light curve or a power spectrum data file and saves the data into `x` and `y`.

    Parameters
    ----------
    path : str
        the file path of the data file
    """
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    # Set values
    x = np.array([float(line.strip().split()[0]) for line in lines])
    y = np.array([float(line.strip().split()[1]) for line in lines])
    return x, y


def check_fitbg(star):
    """Check if there is prior knowledge about numax as SYD needs this information to work well
    (either from findex module or from star info csv).

    Returns
    -------
    result : bool
        will return `True` if there is prior value for numax otherwise `False`.
    """
    if star.params[star.name]['excess']:
        # Check whether output from findex module exists; 
        # if yes, let that override star info guesses
        if glob.glob('%sexcess.csv' % star.params[star.name]['path']) != []:
            df = pd.read_csv('%sexcess.csv' % star.params[star.name]['path'])
            for col in ['numax', 'dnu', 'snr']:
                star.params[star.name][col] = df.loc[0, col]
        # Break if no numax is provided in any scenario
        if star.params[star.name]['numax'] is None:
            print(
                '# ERROR: pySYD cannot run without any value for numax'
            )
            return False
        else:
            return True
    else:
        if star.verbose:
            print(
                '# WARNING: you are not running findex. \n# A value of %.2f muHz was provided for numax.'%star.params[star.name]['numax']
            )
        return True


def get_initial_guesses(star):
    """Get initial guesses for the granulation background."""
    from pysyd.functions import mean_smooth_ind

    # Mask power spectrum for fitbg module based on estimated/fitted numax
    mask = np.ones_like(star.frequency, dtype=bool)
    if star.params[star.name]['lower_b'] is not None:
        mask *= np.ma.getmask(np.ma.masked_greater_equal(star.frequency, star.params[star.name]['lower_b']))
        if star.params[star.name]['upper_b'] is not None:
            mask *= np.ma.getmask(np.ma.masked_less_equal(star.frequency, star.params[star.name]['upper_b']))
        else:
            mask *= np.ma.getmask(np.ma.masked_less_equal(star.frequency, star.nyquist))
    else:
        if star.params[star.name]['numax'] > 300.0:
            mask = np.ma.getmask(np.ma.masked_inside(star.frequency, 100.0, star.nyquist))
        else:
            mask = np.ma.getmask(np.ma.masked_inside(star.frequency, 1.0, star.nyquist))
    # if lower numax adjust default smoothing filter from 2.5->0.5muHz
    if star.params[star.name]['numax'] <= 500.:
        star.fitbg['smooth_ps'] = 0.5
    star.frequency = star.frequency[mask]
    star.power = star.power[mask]
    star.width = star.params['width_sun']*(star.params[star.name]['numax']/star.params['numax_sun'])
    star.times = star.width/star.params[star.name]['dnu']
    # Cut for leaving region out of background fit
    star.maxpower = [
        star.params[star.name]['numax'] - star.times*star.params[star.name]['dnu'],
        star.params[star.name]['numax'] + star.times*star.params[star.name]['dnu']
    ]
    # Bin power spectrum to estimate red noise components
    bin_freq, bin_pow, bin_err = mean_smooth_ind(star.frequency, star.power, star.fitbg['ind_width'])
    # Mask out region with power excess
    star.bin_freq = bin_freq[~((bin_freq > star.maxpower[0]) & (bin_freq < star.maxpower[1]))]
    star.bin_pow = bin_pow[~((bin_freq > star.maxpower[0]) & (bin_freq < star.maxpower[1]))]
    star.bin_err = bin_err[~((bin_freq > star.maxpower[0]) & (bin_freq < star.maxpower[1]))]

    # Use scaling relation from sun to get starting points
    scale = star.params['numax_sun']/((star.maxpower[1] + star.maxpower[0])/2.0)
    taus = np.array(star.params['tau_sun'])*scale
    b = 2.0*np.pi*(taus*1e-6)
    mnu = (1.0/taus)*1e5
    star.b = b[mnu >= min(star.frequency)]
    star.mnu = mnu[mnu >= min(star.frequency)]
    if len(star.mnu)==0:
        star.b = b[mnu >= 10] 
        star.mnu = mnu[mnu >= 10]
    star.nlaws = len(star.mnu)
    star.mnu_orig = np.copy(star.mnu)
    star.b_orig = np.copy(star.b)
    return star


def save_findex(star):
    """Save the results of the find excess routine into the save folder of the current star.

    Parameters
    ----------
    results : list
        the results of the find excess routine
    """
    best = star.findex['results'][star.name]['best']
    variables = ['star', 'numax', 'dnu', 'snr']
    results = [star.name, star.findex['results'][star.name][best]['numax'], star.findex['results'][star.name][best]['dnu'], star.findex['results'][star.name][best]['snr']]
    save_path = '%sexcess.csv' % star.params[star.name]['path']
    ascii.write(np.array(results), save_path, names=variables, delimiter=',', overwrite=True)


def save_fitbg(star):
    """Save results of fit background routine"""
    df = pd.DataFrame(star.fitbg['results'][star.name])
    new_df = pd.DataFrame(columns=['parameter', 'value', 'uncertainty'])
    for c, col in enumerate(df.columns.values.tolist()):
        if 'a_' in col:
            n = int(col.split('_')[-1])
            a = df.loc[0,col]
            a_e = mad_std(df[col].values)
            b = df.loc[0,'b_%d'%n]
            b_e = mad_std(df[col].values)
            sigma = ((a*np.pi)/(2.*b))**(0.5)
            dsdb = 0.5*(((a*np.pi)/(2.*b))**(-0.5))*((a*np.pi)/(2.*(b**2)))
            dsda = 0.5*(((a*np.pi)/(2.*b))**(-0.5))*(np.pi/(2.*b))
            sigma_err = np.sqrt(((dsdb**2)*(b_e**2))+((dsda**2)*(a_e**2)))
            new_df.loc[c, 'parameter'] = 'sigma_%d'%n
            new_df.loc[c, 'value'] = sigma
            if star.fitbg['mc_iter'] > 1:
                new_df.loc[c, 'uncertainty'] = sigma_err
            else:
                new_df.loc[c, 'uncertainty'] = '--'
        elif 'b_' in col:
            n=int(col.split('_')[-1])
            tau = (df.loc[0,col]/(2.*np.pi))*10**-6.
            tau_err = ((mad_std(df[col].values))/(2.*np.pi))*10**-6.
            new_df.loc[c, 'parameter'] = 'tau_%d'%n
            new_df.loc[c, 'value'] = tau
            if star.fitbg['mc_iter'] > 1:
                new_df.loc[c, 'uncertainty'] = tau_err
            else:
                new_df.loc[c, 'uncertainty'] = '--'
        else:
            new_df.loc[c, 'parameter'] = col
            new_df.loc[c, 'value'] = df.loc[0,col]
            if star.fitbg['mc_iter'] > 1:
                new_df.loc[c, 'uncertainty'] = mad_std(df[col].values)
            else:
                new_df.loc[c, 'uncertainty'] = '--'
    new_df.to_csv('%sbackground.csv' % star.params[star.name]['path'], index=False)
    if star.fitbg['samples']:
        df.to_csv('%ssamples.csv' % star.params[star.name]['path'], index=False)


def verbose_output(star, sampling=False):

    if sampling:
        print('\nOutput parameters:')
        print('numax (smoothed): %.2f +/- %.2f muHz' % (star.fitbg['results'][star.name]['numax_smooth'][0], mad_std(star.fitbg['results'][star.name]['numax_smooth'])))
        print('maxamp (smoothed): %.2f +/- %.2f ppm^2/muHz' % (star.fitbg['results'][star.name]['amp_smooth'][0], mad_std(star.fitbg['results'][star.name]['amp_smooth'])))
        print('numax (gaussian): %.2f +/- %.2f muHz' % (star.fitbg['results'][star.name]['numax_gaussian'][0], mad_std(star.fitbg['results'][star.name]['numax_gaussian'])))
        print('maxamp (gaussian): %.2f +/- %.2f ppm^2/muHz' % (star.fitbg['results'][star.name]['amp_gaussian'][0], mad_std(star.fitbg['results'][star.name]['amp_gaussian'])))
        print('fwhm (gaussian): %.2f +/- %.2f muHz' % (star.fitbg['results'][star.name]['fwhm_gaussian'][0], mad_std(star.fitbg['results'][star.name]['fwhm_gaussian'])))
        print('dnu: %.2f +/- %.2f muHz' % (star.fitbg['results'][star.name]['dnu'][0], mad_std(star.fitbg['results'][star.name]['dnu'])))
    else:
        print('-------------------------------------------------')
        print('Output parameters:')
        print('numax (smoothed): %.2f muHz' % (star.fitbg['results'][star.name]['numax_smooth'][0]))
        print('maxamp (smoothed): %.2f ppm^2/muHz' % (star.fitbg['results'][star.name]['amp_smooth'][0]))
        print('numax (gaussian): %.2f muHz' % (star.fitbg['results'][star.name]['numax_gaussian'][0]))
        print('maxamp (gaussian): %.2f ppm^2/muHz' % (star.fitbg['results'][star.name]['amp_gaussian'][0]))
        print('fwhm (gaussian): %.2f muHz' % (star.fitbg['results'][star.name]['fwhm_gaussian'][0]))
        print('dnu: %.2f' % (star.fitbg['results'][star.name]['dnu'][0]))
    print('-------------------------------------------------')
    print()


def scrape_output(args):
    """
    Grabs each individual star's results and concatenates results into a single csv in Files/ for each submodulel
    (i.e. findex.csv and globalpars.csv). This is automatically called at the end of the main SYD module.
    """

    path = '%s/**/'%args.params['outdir']
    # Findex outputs
    output = '%s*excess.csv'%path
    files = glob.glob(output)
    df = pd.read_csv(files[0])
    for i in range(1,len(files)):
        df_new = pd.read_csv(files[i])
        df = pd.concat([df, df_new])
    df.to_csv('%s/excess.csv'%args.params['outdir'], index=False)

    # Fitbg outputs
    output = '%s*background.csv'%path
    files = glob.glob(output)
    df = pd.DataFrame(columns=['star'])

    for i, file in enumerate(files):
	       df_new = pd.read_csv(file)
	       df_new.set_index('parameter',inplace=True,drop=False)
	       df.loc[i,'star']=file.strip().split('/')[-2]
	       new_header_names=[[i,i+'_err'] for i in df_new.index.values.tolist()]
	       new_header_names=list(chain.from_iterable(new_header_names))          
	       for col in new_header_names:
		          if '_err' in col:
			             df.loc[i,col]=df_new.loc[col[:-4],'uncertainty']
		          else:
			             df.loc[i,col]=df_new.loc[col,'value']

    df.fillna('--', inplace=True)
    df.to_csv('%s/background.csv'%args.params['outdir'], index=False)
