### CONFIGURATION ###

# Watch input and output values
DEBUG = True

# Output mode
OUTPUT_FREETRACK = False
OUTPUT_TRACKIR   = True

# Keybindings
KEY_CENTER = Key.Pause      # Center orientation to current position
KEY_TOGGLE_ON_OFF = Key.End # Toggle headtracking on or off

# Calibration multipliers
TRACKIR_MULTIPLIER   = 10
FREETRACK_MULTIPLIER = 0.001

### THE CODE ###

def update():
    global yaw
    yaw = freeImu.yaw
    global pitch
    pitch = freeImu.pitch
    global roll
    roll = freeImu.roll

def updateTrackIR():
    trackIR.yaw = (yaw - centerYaw) * TRACKIR_MULTIPLIER
    trackIR.pitch = (pitch - centerPitch) * TRACKIR_MULTIPLIER
    trackIR.roll = (roll - centerRoll) * TRACKIR_MULTIPLIER

    if DEBUG:
        diagnostics.watch(trackIR.yaw)
        diagnostics.watch(trackIR.pitch)
        diagnostics.watch(trackIR.roll)

def updateFreeTrack():
    freeTrack.yaw = (yaw - centerYaw) * -FREETRACK_MULTIPLIER # Inverted
    freeTrack.pitch = (pitch - centerPitch) * FREETRACK_MULTIPLIER
    freeTrack.roll = (roll - centerRoll) * FREETRACK_MULTIPLIER

    if DEBUG:
        diagnostics.watch(freeTrack.yaw)
        diagnostics.watch(freeTrack.pitch)
        diagnostics.watch(freeTrack.roll)

def center():
    global centerYaw
    centerYaw = yaw
    global centerPitch
    centerPitch = pitch
    global centerRoll
    centerRoll = roll

if starting: 
    enabled = True
    centerYaw = freeImu.yaw
    centerPitch = freeImu.pitch
    centerRoll = freeImu.roll
    
    global yaw
    yaw = 0.0
    global pitch
    pitch = 0.0
    global roll
    roll = 0.0
    freeImu.update += update

def do_update():
    if OUTPUT_FREETRACK:
        updateFreeTrack()
        
    if OUTPUT_TRACKIR:
        updateTrackIR()

if DEBUG:
    diagnostics.watch(yaw)
    diagnostics.watch(pitch)
    diagnostics.watch(roll)

if enabled:
    do_update()

if keyboard.getKeyDown(KEY_CENTER):
    center()
    
if keyboard.getPressed(KEY_TOGGLE_ON_OFF):
    enabled = not enabled
    center()
    do_update()