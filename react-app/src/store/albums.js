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

const normalize = (albumList) => {
    let normAlbums = {};
    for (let i = 0; i < albumList.length; i++) {
        let album = albumList[i];
        normAlbums[album.id] = album;
    }
    return normAlbums;
};

export const retrieveAlbums = () => async (dispatch) => {
    // console.log('BEFORE FETCH')
    let res = await fetch(`/api/albums/allAlbums`);
    // console.log('AFTER FETCH', res.json)

    if (res.ok) {
        const allAlbums = await res.json();

        const albums = normalize(allAlbums.albums)
        dispatch(getAlbums(albums))
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
