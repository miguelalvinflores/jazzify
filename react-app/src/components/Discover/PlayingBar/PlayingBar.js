import React, { useEffect, useRef, useState } from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import './PlayingBar.css'
import AudioControls from './AudioControls'


const PlayingBar = ({tracksQueue}) => {
    const album = useSelector((state) => state.albums.album )
    const artists = useSelector((state => state.artists.allArtists))

    const [trackIndex, setTrackIndex] = useState(0);
    const [trackProgress, setTrackProgress] = useState(0);
    const [trackVolume, setTrackVolume] = useState(1);
    const [isPlaying, setIsPlaying] = useState(false)
    const [isMute, setIsMute] = useState(false);
    // console.log('TRACKSQUEUE', tracksQueue)

    const track = tracksQueue[trackIndex]

    // console.log('TRACK', track)

    const audioRef = useRef(new Audio(track.source_url));
    const intervalRef = useRef();
    const isReady = useRef(false);


    const {duration} = audioRef.current;

    const startTimer = () => {
        // Clear any timers already running
        clearInterval(intervalRef.current);

        intervalRef.current = setInterval(() => {
          if (audioRef.current.ended) {
            toNextTrack();
          } else {
            setTrackProgress(audioRef.current.currentTime);
          }
        }, [1000]);
      }

    useEffect(() => {
        if (isPlaying) {
            audioRef.current.play();
            startTimer();
        } else {
            audioRef.current.pause();
        }
    }, [isPlaying])

    useEffect(() => {
        if(isMute) {
            audioRef.current.muted = true;
        } else {
            audioRef.current.muted = false;
        }
    }, [isMute])

    useEffect(() => {
        return () => {
            audioRef.current.pause();
            clearInterval(intervalRef.current);
            setTrackIndex(0);
        }
    }, [tracksQueue]);

    useEffect(() => {
        audioRef.current.pause();

        audioRef.current = new Audio(track.source_url);
            setTrackProgress(audioRef.current.currentTime);

        if (isReady.current) {
            audioRef.current.play();
            setIsPlaying(true);
            startTimer();

        } else {
            // Set the isReady ref as true for the next pass
            setIsPlaying(true);
            isReady.current = true;
        }
    }, [trackIndex, track]);

    const toPrevTrack = () => {
        if (trackIndex - 1 < 0) {
            setTrackIndex(tracksQueue.length - 1);
          } else {
            setTrackIndex(trackIndex - 1);
          }
    }

    const toNextTrack = () => {
        if (trackIndex < tracksQueue.length - 1) {
            setTrackIndex(trackIndex + 1);
          } else {
            setTrackIndex(0);
          }
    }

    const onMuteClick = () => {
        if(isMute) {
            setIsMute(false)
            setTrackVolume(audioRef.current.volume)
        } else {
            setIsMute(true)
            setTrackVolume(0)
        }

    }

    const onScrub = (value) => {
        // Clear any timers already running
      clearInterval(intervalRef.current);
      audioRef.current.currentTime = value;
      setTrackProgress(audioRef.current.currentTime);
    }

    const onScrubEnd = () => {
      // If not already playing, start
      if (!isPlaying) {
        setIsPlaying(true);
      }
      startTimer();
    }

    const onVolScrub = (value) => {
        audioRef.current.volume = value;
        setIsMute(false);
        setTrackVolume(audioRef.current.volume)
    }

    const calculateTime = (secs) => {
        const minutes = Math.floor(secs / 60);
        const seconds = Math.floor(secs % 60);
        const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
        return `${minutes}:${returnedSeconds}`;
    }

    const currentPercentage = duration ? `${(trackProgress / duration) * 100}%` : '0%';
    const currentVolPercentage = duration ? `${(trackVolume / 1) * 100}%` : '0%';

    let mutesvg = ''
    // useEffect(() => {
        if ((trackVolume / 1) * 100 > 60) {
            mutesvg = (
                <svg role="presentation" height="16" width="16" aria-label="Volume high" id="volume-icon" viewBox="0 0 16 16" className="mute-svg">
                    <path d="M12.945 1.379l-.652.763c1.577 1.462 2.57 3.544 2.57 5.858s-.994 4.396-2.57 5.858l.651.763a8.966 8.966 0 00.001-13.242zm-2.272 2.66l-.651.763a4.484 4.484 0 01-.001 6.397l.651.763c1.04-1 1.691-2.404 1.691-3.961s-.65-2.962-1.69-3.962zM0 5v6h2.804L8 14V2L2.804 5H0zm7-1.268v8.536L3.072 10H1V6h2.072L7 3.732z"></path>
                </svg>
            )
        } else if ((trackVolume / 1) * 100 > 30) {
            mutesvg = (
                <svg role="presentation" height="16" width="16" aria-label="Volume medium" id="volume-icon" viewBox="0 0 16 16" className="mute-svg">
                    <path d="M0 11.032v-6h2.802l5.198-3v12l-5.198-3H0zm7 1.27v-8.54l-3.929 2.27H1v4h2.071L7 12.302zm4.464-2.314q.401-.925.401-1.956 0-1.032-.4-1.957-.402-.924-1.124-1.623L11 3.69q.873.834 1.369 1.957.496 1.123.496 2.385 0 1.262-.496 2.385-.496 1.123-1.369 1.956l-.659-.762q.722-.698 1.123-1.623z"></path>
                </svg>
            )
        } else if ((trackVolume / 1) * 100 > 0) {
            mutesvg = (
                <svg role="presentation" height="16" width="16" aria-label="Volume low" id="volume-icon" viewBox="0 0 16 16" className="mute-svg">
                    <path d="M10.04 5.984l.658-.77q.548.548.858 1.278.31.73.31 1.54 0 .54-.144 1.055-.143.516-.4.957-.259.44-.624.805l-.658-.77q.825-.865.825-2.047 0-1.183-.825-2.048zM0 11.032v-6h2.802l5.198-3v12l-5.198-3H0zm7 1.27v-8.54l-3.929 2.27H1v4h2.071L7 12.302z"></path>
                </svg>
            )
        } else {
            mutesvg = (
                <svg role="presentation" height="16" width="16" aria-label="Volume off" id="volume-icon" viewBox="0 0 16 16" className="mute-svg">
                    <path d="M0 5v6h2.804L8 14V2L2.804 5H0zm7-1.268v8.536L3.072 10H1V6h2.072L7 3.732zm8.623 2.121l-.707-.707-2.147 2.147-2.146-2.147-.707.707L12.062 8l-2.146 2.146.707.707 2.146-2.147 2.147 2.147.707-.707L13.477 8l2.146-2.147z"></path>
                </svg>
            )
        }
    // }, [ trackVolume ])


    const trackStyling = `
        -webkit-gradient(linear, 0% 0%, 100% 0%, color-stop(${currentPercentage}, #382b7f), color-stop(${currentPercentage}, #777))
    `;

    const trackVolStyling = `
    -webkit-gradient(linear, 0% 0%, 100% 0%, color-stop(${currentVolPercentage}, #382b7f), color-stop(${currentVolPercentage}, #777))
    `;

    // const audio = document.querySelector('audio');

    // audio.addEventListener('loadedmetadata', () => {
    //     displayAudioDuration(audio.duration)
    // })

    return (
        <div className='Root__now-playing-bar'>
            {(track && (
                <footer className='play-footer'>
                    <div className='playing-container' >
                        <div className='playing-track-info-container'>
                            <div className='playing-track-info'>
                                <div className='playing-track-img-container'>
                                    <Link to={`/albums/${track?.album_id}`} className='playing-track-img-link' >
                                        <div className='playing-album-img-container'>
                                            <div className='playing-album-cover-art'>
                                                <img className='playing-album-img' src={track?.image_url} alt={`${album.album_title} Album Cover`} />
                                            </div>
                                        </div>
                                    </Link>
                                </div>
                                <div className='playing-track-text-container'>
                                    <div className='playing-track-title'>
                                        <span>
                                            <Link to={`/albums/${track?.album_id}`} className='playing-track-title-link'>
                                                {track?.song_title}
                                            </Link>
                                        </span>
                                    </div>
                                    <div className='playing-track-artist'>
                                        <span>
                                            <span>
                                                {artists[track?.artist_id]?.artist_name}
                                            </span>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className='player-container'>
                            {/* <audio id='audio-player' preload='metadata'>
                                <source src={track.source_url} type="audio/mpeg"></source>
                            </audio> */}
                            <AudioControls
                                isPlaying={isPlaying}
                                onPrevClick={toPrevTrack}
                                onNextClick={toNextTrack}
                                onPlayPauseClick={setIsPlaying}
                            />
                            <div className='player-controls__playback-bar'>
                                <span id="current-time" className="time">{calculateTime(trackProgress)}</span>
                                <div className='progress-bar-wrapper'>
                                    <div className='progress-bar'>
                                        {/* <div className='progress-bar-bg'> */}
                                            {/* <div className='progress-bar-fg-wrapper'> */}
                                                <input
                                                    type="range"
                                                    value={trackProgress}
                                                    step='1'
                                                    min='0'
                                                    max={duration ? duration : `${duration}`}
                                                    className='progress-bar-input'
                                                    onChange={(e) => onScrub(e.target.value)}
                                                    onMouseUp={onScrubEnd}
                                                    onKeyUp={onScrubEnd}
                                                    style={{ background: trackStyling }}
                                                />
                                            {/* </div> */}
                                        {/* </div> */}
                                    </div>
                                </div>
                                <span id="duration" className="time">{duration ? calculateTime(duration) : "0:00"}</span>
                            </div>
                        </div>
                        <div className='extra-controls-container'>
                            <div className='extra-controls'>
                                <div className='extra-controls__volume-bar'>
                                    <button
                                        className='extra-controls__mute-btn'
                                        type='button'
                                        onClick={onMuteClick}
                                    >
                                        {mutesvg}
                                    </button>
                                    <div className='progress-bar-wrapper'>
                                        <div className='progress-bar'>
                                            <input
                                                type='range'
                                                value={trackVolume}
                                                step='.1'
                                                min='0'
                                                max='1'
                                                className='progress-bar-input vol-range'
                                                onChange={(e) => onVolScrub(e.target.value)}
                                                style={{ background: trackVolStyling}}
                                            />
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </footer>
            ))};
        </div>
    );
};

export default PlayingBar;
