const GET_TRACKS_BY_ALBUM = 'track/GET_TRACKS_BY_ALBUM';

const getTracksByAlbum = (tracksByAlbum) => {
    return {
        type: GET_TRACKS_BY_ALBUM,
        payload: tracksByAlbum,
    };
};

export const retrieveTracksByAlbumId = (albumId) => async (dispatch) => {
    let res = await fetch(`/api/tracks/album/${albumId}`);
    console.log(res.json())
    if (res.ok) {
        const albumTracks = await res.json();
        dispatch(getTracksByAlbum(albumTracks));
    }
};

const initialState = {
    albumTracks:{}
}

export default function reducer(state = initialState, action) {
    switch(action.typer) {
        case GET_TRACKS_BY_ALBUM:
            return {
                ...state,
                albumTracks: {...state.albumTracks,...action.payload},
            }
        default:
            return state;
    }
}
