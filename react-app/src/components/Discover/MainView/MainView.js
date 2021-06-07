import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

const MainView = () => {
    const dispatch = useDispatch();
    const user = useSelector((state) => state.sessionUser);

    useEffect(() => {
        if (user) {

        }
    })
    return (
        <div className='Root__main-view'>
            <main className='main-view-container'>
                <div className='main-view-container__scroll-node'>
                    <div className='main-view-container__padding'>
                        <div className='main-view-container__viewport'>
                            <div className='viewport-content'>
                                <div className='main-view-container__scroll-node-child'>
                                    <section className='home-page'>

                                    </section>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
}

export default MainView;
