const GET_TRACKS_BY_ALBUM = 'track/GET_TRACKS_BY_ALBUM';
const PUT_ALBUM_IN_QUEUE = 'track/PUT_ALBUM_IN_QUEUE'
const getTracksByAlbum = (tracksByAlbum) => {
    return {
        type: GET_TRACKS_BY_ALBUM,
        payload: tracksByAlbum,
    };
};

const albumToQueue = (albumTracks) => {
    return {
        type: PUT_ALBUM_IN_QUEUE,
        payload: albumTracks
    }
}

export const retrieveTracksByAlbum = (album) => async (dispatch) => {
    let res = await fetch(`/api/tracks/album/${album.id}`);
    if (res.ok) {
        const albumTracks = await res.json();
        dispatch(getTracksByAlbum(albumTracks));
    }
};

export const playAlbum = (albumTracks) => async (dispatch) => {
    dispatch(albumToQueue(albumTracks))
}

const initialState = {
    trackQueue: [],
    albumTracks:{}
}

export default function reducer(state = initialState, action) {
    switch(action.type) {
        case GET_TRACKS_BY_ALBUM:
            return {
                ...state,
                albumTracks: {...state.albumTracks, ...action.payload},
            }
        case PUT_ALBUM_IN_QUEUE:
            return {
                ...state,
                trackQueue: action.payload
            }
        default:
            return state;
    }
}
