const GET_ALBUMS = 'album/GET_ALBUMS';
const THIS_ALBUM = 'album/THIS_ALBUM';

const thisAlbum = (album) => {
    return {
        type: THIS_ALBUM,
        payload: album,
    };
};

const getAlbums = (allAlbums) => {
    return {
        type: GET_ALBUMS,
        payload: allAlbums,
    };
};

export const retriveAlbums = () => async (dispatch) => {
    let res = await fetch(`/api/albums/allAlbums`);

    if (res.ok) {
        const allAlbums = await res.json();

        dispatch(getAlbums(allAlbums))
    }

    return res;
};

export const chooseAlbum = () => async (dispatch) => {
    let res = await fetch(`/api/albums/album`);

    if (res.ok) {
        const album = await res.json();
        dispatch(thisAlbum(album));
    }
};

const initialState = {
    album: {},
    allAlbums: {},
};

export default function reducer(state = initialState, action) {
    switch(action.type) {
        case THIS_ALBUM:
            return {
                ...state,
                album: action.payload,
            };
        case GET_ALBUMS:
            return {
                ...state,
                allAlbums: { ...state.allAlbums, ...action.payload},
            };
        default:
            return state;
    }
}
