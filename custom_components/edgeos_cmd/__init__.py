DOMAIN = 'edgeos_cmd'

def setup(hass, config):
    hass.states.set('edgeos_cmd.init', 'True')

    # Return boolean to indicate that initialization was successful.
    return True