(self["webpackChunkjupyterlab_frontegg"] = self["webpackChunkjupyterlab_frontegg"] || []).push([["lib_index_js"],{

/***/ "./lib/components/LandingPage/LandingPage.js":
/*!***************************************************!*\
  !*** ./lib/components/LandingPage/LandingPage.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "./node_modules/react/jsx-runtime.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-router-dom */ "webpack/sharing/consume/default/react-router-dom/react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _material_ui_core_styles__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @material-ui/core/styles */ "./node_modules/@material-ui/core/esm/styles/makeStyles.js");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @material-ui/core */ "webpack/sharing/consume/default/@material-ui/core/@material-ui/core");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _material_ui_core_Paper__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/core/Paper */ "./node_modules/@material-ui/core/esm/Paper/Paper.js");
/* harmony import */ var _Login_Login__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ../Login/Login */ "./lib/components/Login/Login.js");


// import { Button } from "@material-ui/core";





// import './landingPage.css';
const useStyles = (0,_material_ui_core_styles__WEBPACK_IMPORTED_MODULE_4__.default)((theme) => ({
    submitBtn: {
        backgroundColor: '#82abee',
        color: '#fff',
        width: '55%',
        // marginTop: '4%',
        // marginBottom: '2%'
        padding: '7px 0',
        backgroundColor: '#3c78d8',
        borderRadius: '5px',
        fontWeight: 'bold',
        fontSize: '16px',
        border: 'none',
        marginBottom: '10%'
    },
    paper: {
        padding: theme.spacing(2),
        textAlign: 'center',
        // color: theme.palette.text.secondary,
        width: '30%',
        // marginTop: '5%',
        marginLeft: '35%',
        // backgroundColor: 'whitesmoke',
        borderRadius: '5%'
    },
}));
function LoginSuccess(props) {
    const classes = useStyles();
    const history = (0,react_router_dom__WEBPACK_IMPORTED_MODULE_2__.useHistory)();
    const [OpenModal, setOpenModal] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(false);
    const { authenticate, setAuthenticate } = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(false);
    const [open, setOpen] = react__WEBPACK_IMPORTED_MODULE_1___default().useState(true);
    const handleWaitList = () => {
        setOpenModal(true);
    };
    const handleClose = () => {
        setOpen(false);
        // window.location.reload();
        // }
    };
    return ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, { children: authenticate ?
            (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", Object.assign({ style: { marginTop: "6%" } }, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("img", { style: { width: '15%' }, src: "https://img1.wsimg.com/isteam/ip/5944b92b-9cdf-4e95-9400-d95080c03bdb/Weav%20Logo%20-%200.6.png/:/rs=h:640/ll" }, void 0),
                    (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("p", Object.assign({ style: { textAlign: "center", fontSize: "20px" } }, { children: "WEAV AI" }), void 0), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("br", {}, void 0),
                    (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__.Grid, Object.assign({ container: true, spacing: 3 }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(_material_ui_core_Paper__WEBPACK_IMPORTED_MODULE_5__.default, Object.assign({ className: classes.paper }, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("h3", { children: user === null || user === void 0 ? void 0 : user.name }, void 0),
                                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("h3", { children: user === null || user === void 0 ? void 0 : user.email }, void 0),
                                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("h3", { children: user === null || user === void 0 ? void 0 : user.id }, void 0),
                                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("button", Object.assign({ onClick: handleWaitList, style: { textAlign: "center", cursor: 'pointer' }, className: classes.submitBtn }, { children: "Logout" }), void 0)] }), void 0) }), void 0)] }), void 0)
            :
                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", Object.assign({ style: { marginTop: "6%" } }, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("img", { style: { width: '15%' }, src: "https://img1.wsimg.com/isteam/ip/5944b92b-9cdf-4e95-9400-d95080c03bdb/Weav%20Logo%20-%200.6.png/:/rs=h:640/ll" }, void 0),
                        (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("p", Object.assign({ style: { textAlign: "center", fontSize: "20px" } }, { children: "WEAV AI" }), void 0), (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("br", {}, void 0),
                        (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__.Grid, Object.assign({ container: true, spacing: 3 }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(_material_ui_core_Paper__WEBPACK_IMPORTED_MODULE_5__.default, Object.assign({ className: classes.paper }, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("h2", { children: "Interested?" }, void 0),
                                    (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("button", Object.assign({ onClick: handleWaitList, style: { textAlign: "center", cursor: 'pointer' }, className: classes.submitBtn }, { children: "Join the Waitlist !" }), void 0)] }), void 0) }), void 0),
                        OpenModal ? (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_Login_Login__WEBPACK_IMPORTED_MODULE_6__.default, { open: handleClose }, void 0) : ''] }), void 0) }, void 0));
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (LoginSuccess);


/***/ }),

/***/ "./lib/components/Login/Login.js":
/*!***************************************!*\
  !*** ./lib/components/Login/Login.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "./node_modules/react/jsx-runtime.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @material-ui/core */ "webpack/sharing/consume/default/@material-ui/core/@material-ui/core");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__);




const axios = __webpack_require__(/*! axios */ "webpack/sharing/consume/default/axios/axios").default;
const useStyles = (0,_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.makeStyles)((theme) => ({
    modal: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '550px',
        margin: 'auto',
        borderRadius: '5px',
        border: 'none'
    },
    paper: {
        backgroundColor: theme.palette.background.paper,
        border: '2px solid #000',
        boxShadow: theme.shadows[5],
        padding: theme.spacing(2, 4, 3),
        width: 'auto',
    },
    head: {
        backgroundColor: '#41B2CC',
        color: '#fff',
        height: 60,
        width: '100%',
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontSize: 18,
        fontWeight: "500",
        borderRadius: '8px 8px 0 0'
    },
    SectionWrap: {
        width: 400,
        borderRadius: 8
    },
    paymentSelectBody: {
        padding: '5%'
    },
    inputField: {
        width: '55%',
        marginTop: '2%',
        height: '8%'
    },
    submitBtn: {
        // backgroundColor: '#82abee',
        color: '#fff',
        width: '55%',
        marginTop: '4%',
        // marginBottom: '2%'
        padding: '7px 0',
        backgroundColor: '#3c78d8',
        borderRadius: '5px',
        fontWeight: 'bold',
        fontSize: '16px',
        border: 'none',
    },
    gitHubBtn: {
        backgroundColor: '#363030',
        color: '#fff',
        width: '55%',
        marginTop: '2%',
        // marginBottom: '2%'
        padding: '7px 0',
        borderRadius: '5px',
        // fontWeight: 'bold',
        fontSize: '14px',
        border: 'none',
    },
}));
function Login(props) {
    const classes = useStyles();
    const [open, setOpen] = react__WEBPACK_IMPORTED_MODULE_1___default().useState(true);
    const [disabled, setDisabled] = react__WEBPACK_IMPORTED_MODULE_1___default().useState(false);
    const [showFedback, setshowFedback] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(false);
    const [details, setdetails] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)({ name: "", email: "", password: "", companyName: "" });
    const [errorMessage, setErrorMessage] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)("");
    const [error, setError] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(false);
    const [success, setSuccess] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(false);
    const [token, setToken] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)('');
    const handlefeedback = () => {
        setshowFedback(true);
    };
    const handleClose = () => {
        setOpen(false);
        props.open(false);
    };
    (0,react__WEBPACK_IMPORTED_MODULE_1__.useEffect)(() => {
        axios({
            method: 'POST',
            data: {
                "clientId": "755ebd69-116e-4e21-8af0-28d507a4cb38",
                "secret": "b67b00de-b590-4ab6-b80c-da1095665284"
            },
            url: "https://api.frontegg.com/auth/vendor/",
        })
            .then(async function (response) {
            if (response.status && response.status == '200') {
                setToken(response.data.token);
            }
        })
            .catch(function (error) {
            console.log('error::::::::', error);
        });
    }, []);
    const handleAddList = () => {
        if (details.name === "" && details.email === "") {
            setErrorMessage("Please fill all details");
            setError(true);
        }
        else if (details.name === "") {
            setErrorMessage("Please fill Name");
        }
        else if (details.email === "") {
            setErrorMessage("Please fill Email");
        }
        else {
            setError(false);
            setSuccess(true);
        }
        axios({
            method: 'POST',
            data: details,
            headers: {
                'authorization': `Bearer ${token}`,
            },
            url: "https://api.frontegg.com/identity/resources/users/v1/signUp",
        })
            .then(async function (response) {
            if (response.status && response.status == '201') {
                console.log(response.data.data);
            }
        })
            .catch(function (error) {
            console.log('error::::::::', error);
        });
    };
    const handleDetails = (event) => {
        if (event.target.name === "name") {
            setdetails((preValue) => {
                return {
                    name: event.target.value,
                    email: preValue.email,
                    password: preValue.password,
                    companyName: preValue.companyName
                };
            });
        }
        else if (event.target.name === "email") {
            setdetails((preValue) => {
                return {
                    name: preValue.name,
                    email: event.target.value,
                    password: preValue.password,
                    companyName: preValue.companyName
                };
            });
        }
        else if (event.target.name === "password") {
            setdetails((preValue) => {
                return {
                    name: preValue.name,
                    email: preValue.email,
                    password: event.target.value,
                    companyName: preValue.companyName
                };
            });
        }
        else {
            setdetails((preValue) => {
                return {
                    name: preValue.name,
                    email: preValue.email,
                    password: preValue.password,
                    companyName: event.target.value
                };
            });
        }
        setError(false);
    };
    return ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.Modal, Object.assign({ disableBackdropClick: true, disableAutoFocus: true, "aria-labelledby": "spring-modal-title", "aria-describedby": "spring-modal-description", className: classes.modal, open: open, onClose: handleClose, closeAfterTransition: true, BackdropComponent: _material_ui_core__WEBPACK_IMPORTED_MODULE_2__.Backdrop, BackdropProps: {
            timeout: 500,
        } }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("div", Object.assign({ className: classes.paper, id: "checkout" }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", Object.assign({ className: classes.SectionWrap }, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("div", Object.assign({ style: { textAlign: "end" } }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("button", Object.assign({ className: "payclose", onClick: handleClose, style: { marginRight: "20px", marginTop: "-45px", cursor: 'pointer' } }, { children: "x" }), void 0) }), void 0),
                    !success ?
                        (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", Object.assign({ style: { textAlign: "center" } }, { children: [(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.Grid, Object.assign({ item: true, xs: 12 }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.TextField, { className: classes.inputField, name: "name", placeholder: "Enter Name", id: "outlined-basic", label: "Name", variant: "outlined", onChange: handleDetails }, void 0) }), void 0),
                                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.Grid, Object.assign({ item: true, xs: 12 }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.TextField, { className: classes.inputField, type: "email", name: "email", id: "outlined-basic", placeholder: "Enter E-mail", label: "Email", variant: "outlined", onChange: handleDetails }, void 0) }), void 0),
                                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.Grid, Object.assign({ item: true, xs: 12 }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.TextField, { className: classes.inputField, type: "password", name: "password", id: "outlined-basic", placeholder: "Enter Password", label: "Password", variant: "outlined", onChange: handleDetails }, void 0) }), void 0),
                                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.Grid, Object.assign({ item: true, xs: 12 }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_material_ui_core__WEBPACK_IMPORTED_MODULE_2__.TextField, { className: classes.inputField, name: "companyName", id: "outlined-basic", placeholder: "Enter company Name", label: "Company Name", variant: "outlined", onChange: handleDetails }, void 0) }), void 0),
                                error ? (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("p", Object.assign({ style: { color: 'red' } }, { children: errorMessage }), void 0) : "",
                                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("button", Object.assign({ onClick: handleAddList, style: { textAlign: "center", cursor: 'pointer' }, className: classes.submitBtn }, { children: "Add me to the list !" }), void 0),
                                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("h2", { children: "OR" }, void 0),
                                (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("button", Object.assign({ 
                                    // onClick={handleWaitList}
                                    style: { textAlign: "center", cursor: 'pointer' }, className: classes.gitHubBtn }, { children: "Sign In with GitHub" }), void 0)] }), void 0)
                        :
                            (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("div", { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("h2", Object.assign({ style: { textAlign: "center" } }, { children: ["Thank You ", details.name, "!", (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("br", {}, void 0), " You will hear from us as soon as your account is approved. ", (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("br", {}, void 0), "Stay Tuned!"] }), void 0) }, void 0)] }), void 0) }), void 0) }), void 0));
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Login);


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./widget */ "./lib/widget.js");


// import { reactIcon } from '@jupyterlab/ui-components';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

// import logo from './Logo.png';
/**
 * The command IDs used by the react-widget plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.create = 'create-react-widget';
})(CommandIDs || (CommandIDs = {}));
/**
 * Initialization data for the react-widget extension.
 */
const extension = {
    id: 'react-widget',
    autoStart: true,
    optional: [_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__.ILauncher],
    activate: (app, launcher) => {
        const { commands } = app;
        const command = CommandIDs.create;
        commands.addCommand(command, {
            caption: 'WEAV AI launcher',
            label: 'WEAV AI',
            icon: args => (args['isPalette'] ? null : null),
            execute: () => {
                const content = new _widget__WEBPACK_IMPORTED_MODULE_2__.CounterWidget();
                const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.MainAreaWidget({ content });
                widget.title.label = 'WEAV AI';
                // widget.title.icon = reactIcon
                app.shell.add(widget, 'main');
            }
        });
        if (launcher) {
            launcher.add({
                command
            });
        }
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CounterWidget": () => (/* binding */ CounterWidget)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-runtime */ "./node_modules/react/jsx-runtime.js");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _components_LandingPage_LandingPage__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./components/LandingPage/LandingPage */ "./lib/components/LandingPage/LandingPage.js");



/**
 * A Counter Lumino Widget that wraps a CounterComponent.
 */
class CounterWidget extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ReactWidget {
    /**
     * Constructs a new CounterWidget.
     */
    constructor() {
        super();
        this.addClass('jp-ReactWidget');
    }
    render() {
        return ((0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)("div", Object.assign({ style: { textAlign: "center" } }, { children: (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx)(_components_LandingPage_LandingPage__WEBPACK_IMPORTED_MODULE_2__.default, {}, void 0) }), void 0));
    }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.b1ab1cab32624e785fb4.js.map