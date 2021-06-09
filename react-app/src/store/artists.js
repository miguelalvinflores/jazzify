const GET_ARTISTS = 'artist/GET_ARTISTS';

const getArtists = (allArtists) => {
    return {
        type: GET_ARTISTS,
        payload: allArtists,
    };
};

const normalize = (artistList) => {
    let normArtists = {};

    for (let i = 0; i < artistList.length; i++) {
        let artist = artistList[i];
        normArtists[artist.id] = artist;
    }

    return normArtists
}

export const retrieveArtists = () => async (dispatch) => {

    let res = await fetch(`/api/artists/allArtists`);

    if (res.ok) {
        const allArtists = await res.json();

        const artists = normalize(allArtists.artists)
        dispatch(getArtists(artists))
    }

    return res;
};

const initialState = {
    allArtists: {},
};


export default function reducer(state = initialState, action) {
    switch(action.type) {
        case GET_ARTISTS:
            return {
                ...state,
                allArtists: {...state.allArtists, ...action.payload},
            };
        default:
            return state;
    }
}
