function fn_CatchError(ex) {
    console.log(ex)
    notie.alert({ type: 'error', text: `${ex}`, stay: false, position: 'bottom' })
}

function fn_ErrorFound(err) {
    notie.alert({ type: 'error', text: `${err}`, stay: false, position: 'bottom' })
}

function fn_EncryptResponse(response) {
    try {
        if (response.status >= 200 && response.status < 300) {
            let clone = response.clone();
            var data = clone.json();
            return Promise.resolve(data).then(function (res) { return res });
        } else {
            return Promise.reject(new Error(response.statusText))
        }
    } catch (objErrorText) {
        fn_CatchError(objErrorText);
    }
}


async function fn_GetAsyncCall(api) {
    var response = await fetch(api, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            "Authorization": "Token ae6365791869a7cae9caa0411a659f5090bf8397"
        }
    }).then(fn_EncryptResponse).then(function (response) {
        return response
    }).catch(function (err) {
        console.log(err)
        return { 'ok': 0, "error": err }
    });

    return response;
}

async function fn_PostAsyncCall(api, jsonBody) {
    var response = fetch(api, {
        method: 'POST',
        body: jsonBody,
        headers: {
            'Content-Type': 'application/json',
            "authorization": "token ae6365791869a7cae9caa0411a659f5090bf8397"
        }
    }).then(fn_EncryptResponse).then(function (response) {
        return response
    }).catch(function (err) {
        return { 'ok': 0, "error": err }
    });

    return response;
}

async function fn_PatchAsyncCall(api, jsonBody) {
    var response = fetch(api, {
        method: 'PATCH',
        body: jsonBody,
        headers: {
            'Content-Type': 'application/json',
            "authorization": "token ae6365791869a7cae9caa0411a659f5090bf8397"
        }
    }).then(fn_EncryptResponse).then(function (response) {
        return response
    }).catch(function (err) {
        return { 'ok': 0, "error": err }
    });

    return response;
}

async function fn_DeleteAsyncCall(api) {
    var response = fetch(api, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            "authorization": "token ae6365791869a7cae9caa0411a659f5090bf8397"
        }
    }).then(fn_EncryptResponse).then(function (response) {
        return response
    }).catch(function (err) {
        return { 'ok': 0, "error": err }
    });

    return response;
}
