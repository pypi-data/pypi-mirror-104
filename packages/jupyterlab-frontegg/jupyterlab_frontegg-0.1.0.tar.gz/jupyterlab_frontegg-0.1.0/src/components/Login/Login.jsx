import React, { useState, useEffect } from 'react';
import { makeStyles, Button, Typography, Card, CardContent, Grid } from '@material-ui/core';
import { Modal, Backdrop, TextField, Snackbar } from '@material-ui/core';
import { render } from 'react-dom';
const axios = require('axios').default;


const useStyles = makeStyles((theme) => ({
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
    // marginBottom: '10%'
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
  const [open, setOpen] = React.useState(true);
  const [disabled, setDisabled] = React.useState(false)
  const [showFedback, setshowFedback] = useState(false)
  const [details, setdetails] = useState({ name: "", email: "", password: "", companyName: "" })
  const [errorMessage, setErrorMessage] = useState("");
  const [error, setError] = useState(false)
  const [success, setSuccess] = useState(false)
  const [token, setToken] = useState('')

  
  const handlefeedback = () => {
    setshowFedback(true)
  }

  const handleClose = () => {
    setOpen(false)
    props.open(false)
  };

  useEffect(()=>{
    axios({
      method: 'POST',
      data: {
        "clientId":"755ebd69-116e-4e21-8af0-28d507a4cb38",
        "secret": "b67b00de-b590-4ab6-b80c-da1095665284"
    },
     
      url: "https://api.frontegg.com/auth/vendor/",
     })
      .then(async function (response) {
          if (response.status && response.status == '200') {
              setToken(response.data.token)
          } 
      })
      .catch(function (error) {
          console.log('error::::::::', error)
      })
  }, [])

  const handleAddList = () => {
    if (details.name === "" && details.email === "") {
      setErrorMessage("Please fill all details")
      setError(true)
    } else if (details.name === "") {
      setErrorMessage("Please fill Name")
    } else if (details.email === "") {
      setErrorMessage("Please fill Email")
    } else {
      setError(false)
      setSuccess(true)
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
          console.log('error::::::::', error)
      })
  };

  const handleDetails = (event) => {
    if (event.target.name === "name") {
      setdetails((preValue)=>{
        return {
          name: event.target.value,
          email: preValue.email,
          password: preValue.password,
          companyName: preValue.companyName
        }
      })
    } else if(event.target.name === "email") {
      setdetails((preValue)=>{
        return {
          name: preValue.name,
          email: event.target.value,
          password: preValue.password,
          companyName: preValue.companyName
        }
      })
    } else if(event.target.name === "password"){
      setdetails((preValue)=>{
        return {
          name: preValue.name,
          email: preValue.email,
          password: event.target.value,
          companyName: preValue.companyName
        }
      })
    } else {
      setdetails((preValue)=>{
        return {
          name: preValue.name,
          email: preValue.email,
          password: preValue.password,
          companyName: event.target.value
        }
      })
    }
    setError(false)
  };
 
  return (

    <Modal
      disableBackdropClick
      disableAutoFocus
      aria-labelledby="spring-modal-title"
      aria-describedby="spring-modal-description"
      className={classes.modal}
      open={open}
      onClose={handleClose}
      closeAfterTransition
      BackdropComponent={Backdrop}
      BackdropProps={{
        timeout: 500,
      }}
    >
      <div className={classes.paper} id="checkout">
        <div
          className={classes.SectionWrap}
        >
          <div style={{ textAlign: "end" }}>
            <button
              className="payclose"
              onClick={handleClose}
              style={{ marginRight: "20px", marginTop: "-45px", cursor: 'pointer' }}
            >
              x
              </button>
          </div>
          {!success ?
            <div style={{ textAlign: "center" }}>
              <Grid item xs={12}>
                <TextField className={classes.inputField} name="name" placeholder="Enter Name" id="outlined-basic" label="Name" variant="outlined" onChange={handleDetails} />
              </Grid>
              <Grid item xs={12}>
                <TextField className={classes.inputField} type="email" name="email" id="outlined-basic" placeholder="Enter E-mail" label="Email" variant="outlined" onChange={handleDetails} />
              </Grid>
              <Grid item xs={12}>
                <TextField className={classes.inputField} type="password" name="password" id="outlined-basic" placeholder="Enter Password" label="Password" variant="outlined" onChange={handleDetails} />
              </Grid>
              <Grid item xs={12}>
                <TextField className={classes.inputField}  name="companyName" id="outlined-basic" placeholder="Enter company Name" label="Company Name" variant="outlined" onChange={handleDetails} />
              </Grid>
              {error ? <p style={{ color: 'red' }}>{errorMessage}</p> : ""}
              <button
                onClick={handleAddList}
                style={{ textAlign: "center", cursor: 'pointer' }}
                className={classes.submitBtn}
              >
                Add me to the list !
      </button>
              <h2>OR</h2>
              <button
                // onClick={handleWaitList}
                style={{ textAlign: "center", cursor: 'pointer' }}
                className={classes.gitHubBtn}
              >
                Sign In with GitHub
      </button>
            </div>

            :
            <div>
              <h2 style={{ textAlign: "center" }}>Thank You {details.name}!<br /> You will hear from us as soon as your account is approved. <br />Stay Tuned!</h2>
            </div>
          }
        </div>
      </div>

    </Modal>
  )
}

export default Login
