from flask.cli import AppGroup
from .users import seed_users, undo_users
from .albums import seed_albums, undo_albums
from .artists import seed_artists, undo_artists
from .tracks import seed_tracks, undo_tracks

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_artists()
    seed_albums()
    seed_tracks()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_tracks()
    undo_albums()
    undo_artists()
    undo_users()

    # Add other undo functions here
