import React, {useState} from "react";
// import { Button } from "@material-ui/core";
import {Redirect, useHistory} from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import {Button, Grid, Typography, TextareaAutosize, TextField, Modal } from '@material-ui/core';
import Paper from '@material-ui/core/Paper';
import Login from '../Login/Login';
// import './landingPage.css';


const useStyles = makeStyles((theme) => ({
    submitBtn:{
        backgroundColor: '#82abee',
        color:'#fff',
        width:'55%',
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
    const history = useHistory();
    const [OpenModal, setOpenModal] = useState(false)
    const { authenticate, setAuthenticate } = useState(false);
    const [open, setOpen] = React.useState(true);

    const handleWaitList = () => {

    setOpenModal(true)

  };

 const handleClose = () => {
        setOpen(false)
        // window.location.reload();
    // }
};

  return (
    <>
    {authenticate ? 
    
      <div style={{marginTop:"6%"}}>
         <img style={{width: '15%'}} src="https://img1.wsimg.com/isteam/ip/5944b92b-9cdf-4e95-9400-d95080c03bdb/Weav%20Logo%20-%200.6.png/:/rs=h:640/ll" />
        <p style={{textAlign:"center",fontSize: "20px"}}>WEAV AI</p><br/>

        <Grid container  spacing={3}>
            <Paper className={classes.paper}>
        <h3>{user?.name}</h3>
        <h3>{user?.email}</h3>
        <h3>{user?.id}</h3>
        <button
        onClick={handleWaitList}
        style={{textAlign:"center", cursor: 'pointer' }}
        className={classes.submitBtn}
        // className="submitBtn"
      >
       Logout
      </button>
      </Paper>
      </Grid>
    </div>
     : 
      <div style={{marginTop:"6%"}}>
         <img style={{width: '15%'}} src="https://img1.wsimg.com/isteam/ip/5944b92b-9cdf-4e95-9400-d95080c03bdb/Weav%20Logo%20-%200.6.png/:/rs=h:640/ll" />
        <p style={{textAlign:"center",fontSize: "20px"}}>WEAV AI</p><br/>

        <Grid container  spacing={3}>
            <Paper className={classes.paper}>
        <h2>Interested?</h2>
      <button
        onClick={handleWaitList}
        style={{textAlign:"center",  cursor: 'pointer' }}
        className={classes.submitBtn}
        // className="submitBtn"
      >
        Join the Waitlist !
      </button>
      </Paper>
      </Grid>
      {OpenModal ? <Login open={handleClose}/> : ''}
    </div>}
    </>
    
  );
}

export default LoginSuccess;
