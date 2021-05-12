import React, {useState} from 'react';

import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

import SearchButton from './SearchButton'
import SearchTextField from './SearchTextField'
import ControlSearch from './ControlSearch'

const useStyles = makeStyles({
  table: {
    minWidth: 650,
    height: '700px'
  },
  container: {
    maxHeight: '80vh',
    maxWidth: '99vw',
    marginTop: '5px',
    marginLeft: '10px',
    marginRight: '10px'
  },
  button: {
    height: '55px',
    margin: '5px',
    marginTop: '30px'
  },
  text: {
    height: '60px',
    margin: '5px',
    marginTop: '30px'
  },
  row: {
    verticalAlign: "top"
  }
});


export default function Result({data,refetch,setQueryValue, setSearchValueMode}) {
  const classes = useStyles();
  const [searchValue, setSearchValue] = useState("default")
  const [searchMode, setSearchMode] = useState("exact")

  const refetchQuery =  () => {
    setQueryValue(searchValue)
    setSearchValueMode(searchMode)
    refetch({ params: { refresh: true } })
  }

  return (
    <div>
        <Grid
            container
            direction="row"
            justify="center"
            alignItems="center"
          >
            <SearchTextField setSearchValue={setSearchValue} />
            <ControlSearch setSearchMode={setSearchMode}/>
            <SearchButton refetch={refetchQuery} />
            
        </Grid>
        <TableContainer component={Paper} className={classes.container}>
            <Table stickyHeader aria-label="sticky table" className={classes.table}>
                <TableHead>
                <TableRow>
                    <TableCell>City_Name</TableCell>
                    <TableCell align="right">City_Code</TableCell>
                    <TableCell align="right">Province_Code</TableCell>
                    <TableCell align="right">Suppressed</TableCell>
                </TableRow>
                </TableHead>
                <TableBody>
                {data.map((row) => (
                    <TableRow className={classes.row} key={row.name}>
                    <TableCell component="th" scope="row">
                        {row.City_Name}
                    </TableCell>
                    <TableCell align="right">{row.City_Code}</TableCell>
                    <TableCell align="right">{row.Province_Code}</TableCell>
                    <TableCell align="right">{row.Suppressed ? "yes" : "no"}</TableCell>
                    </TableRow>
                ))}
                </TableBody>
            </Table>
            </TableContainer>
 
        
    </div>
   
  );
}