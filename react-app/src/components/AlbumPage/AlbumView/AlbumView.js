import React from 'react';
import { usePalette } from 'react-palette'
import { useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';
import './AlbumView.css'

const AlbumView = () => {
    const { albumId } = useParams();
    const album = useSelector((state) => state.albums.allAlbums[albumId]);
    // console.log(album,'ALBUM AT APAGE')
    const { data, loading, error } = usePalette(album.image_url)
    console.log(data.vibrant)
    return (
        <div className='Root__album-view'>
            <main className='album-view-container'>
            <div className='album-view-container__scroll-node'>
                    <div className='album-view-container__padding'>
                        <div className='album-view-container__viewport'>
                            <div className='viewport-content' style={{padding: "0px"}, {height: "100%"}, {width: "100%"}}>
                                <div className='album-view-container__scroll-node-child'>
                                    <section className='album-page'>
                                        {/* <div className='ap-container'> */}
                                            <div className='contentSpacing'>
                                                <div style={{ backgroundColor: data.vibrant }} className='billboard-background'>

                                                </div>
                                            </div>
                                        {/* </div> */}
                                    </section>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    )
}

export default AlbumView;
