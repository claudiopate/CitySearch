import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';

const useStyles = makeStyles({
    text: {
        height: '60px',
        margin: '5px',
        marginTop: '30px'
    }
});


export default function SearchTextField({setSearchValue}) {
    
    const classes = useStyles()
    return(
       
        <TextField className={classes.text} id="outlined-basic" label="Insert the city name" variant="outlined" onChange={(event) => setSearchValue(event.target.value)} />
        
    );
}