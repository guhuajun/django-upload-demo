import axios from 'axios';

let util = {

};
util.title = function (title) {
    title = title ? title + ' - Home' : 'iView project';
    window.document.title = title;
};

const ajaxUrl = 'http://demo.corp.contoso.com';

util.ajax = axios.create({
    baseURL: ajaxUrl,
    timeout: 30000
});

export default util;