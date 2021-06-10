import React from 'react';
const AudioControls = ({
    isPlaying,
    onPlayPauseClick,
    onPrevClick,
    onNextClick,
}) => (
    <div className='player-controls'>
        <div className='player-controls__buttons'>
            <div className='player-controls__left'>
                <button
                    className='player-controls__previous'
                    type="button"
                    onClick={onPrevClick}
                >
                    <svg role="img" height="16" width="16" viewBox="0 0 16 16" className="previous-svg">
                        <path d="M13 2.5L5 7.119V3H3v10h2V8.881l8 4.619z"></path>
                    </svg>
                </button>
            </div>
            { isPlaying?
            (<button
                type='button'
                className='player-controls__pause'
                onClick={() => onPlayPauseClick(false)}
            >
                <svg role="img" height="16" width="16" viewBox="0 0 16 16" className="pause-svg">
                    <path fill="none" d="M0 0h16v16H0z"></path>
                    <path d="M3 2h3v12H3zm7 0h3v12h-3z"></path>
                </svg>
            </button>)
            :
            (<button
                type='button'
                className='player-controls__play'
                onClick={() => onPlayPauseClick(true)}
            >
                <svg role="img" height="16" width="16" viewBox="0 0 16 16" className="play-svg">
                    <path d="M4.018 14L14.41 8 4.018 2z"></path>
                </svg>
            </button>)
            }
            <div className='player-controls__right'>
                <button
                    type='button'
                    className='player-controls__next'
                    onClick={onNextClick}
                >
                    <svg role="img" height="16" width="16" viewBox="0 0 16 16" className="next-svg">
                        <path d="M11 3v4.119L3 2.5v11l8-4.619V13h2V3z"></path>
                    </svg>
                </button>
            </div>
        </div>

    </div>
)

export default AudioControls;
