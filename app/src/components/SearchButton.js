import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles({
    button: {
        height: '55px',
        margin: '5px',
        marginTop: '30px'
      }
});


export default function SearchButton({refetch}) {

    const classes = useStyles()
    return(
       
        <Button className={classes.button} variant="contained" color="primary" onClick={refetch}>
            Search
        </Button>
    );
}