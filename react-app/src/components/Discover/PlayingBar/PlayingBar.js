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
    const [isPlaying, setIsPlaying] = useState(false)
    console.log('TRACKSQUEUE', tracksQueue)

    const track = tracksQueue[trackIndex]

    console.log('TRACK', track)

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

    const calculateTime = (secs) => {
        const minutes = Math.floor(secs / 60);
        const seconds = Math.floor(secs % 60);
        const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
        return `${minutes}:${returnedSeconds}`;
      }

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
                                        />
                                    </div>
                                </div>
                                <span id="duration" className="time">{duration ? calculateTime(duration) : "0:00"}</span>
                            </div>
                        </div>
                        <div className='extra-controls-container'>
                            <div className='extra-controls'>
                                <div className='extra-controls__volume-bar'>

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
