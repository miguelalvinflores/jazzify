import React from 'react';
import './AlbumView.css'

const AlbumView = () => {
    return (
        <div className='Root__album-view'>
            <main className='album-view-container'>
            <div className='album-view-container__scroll-node'>
                    <div className='album-view-container__padding'>
                        <div className='album-view-container__viewport'>
                            <div className='viewport-content' style={{padding: "0px"}, {height: "100%"}, {width: "100%"}}>
                                <div className='album-view-container__scroll-node-child'>
                                    <section className='album-page'>
                                        <div className='ap-container'>
                                            <div className='content-spacing'>
                                                <section className='recommended-section'>
                                                    
                                                </section>
                                                <section>

                                                </section>
                                                <section>

                                                </section>
                                                <section>

                                                </section>
                                            </div>
                                        </div>
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
