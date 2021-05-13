import './App.css';
import { Get } from 'react-axios'
import {useState} from 'react';
import CircularProgress from '@material-ui/core/CircularProgress'
import Result from './components/Result'


function App() {

  const [queryValue, setQueryValue] = useState("default")
  const [searchValueMode, setSearchValueMode] = useState("exact")

  var api_name = "search"
  if (queryValue.match(/^\d/)) {
    console.log(queryValue);
    api_name = "search_by_code"
  }

  var url = "http://localhost:5000/" + api_name + "/" + queryValue
  if(searchValueMode === "startWith")
    url = "http://localhost:5000/" + api_name + "/" + queryValue + "*"
  else if(searchValueMode === "endWith")
    url = "http://localhost:5000/" + api_name + "/*" + queryValue 
  else if(searchValueMode === "contain")
    url = "http://localhost:5000/" + api_name + "/*" + queryValue + "*"
  
  return (
    <div className="App">
      <Get url={url}>
        {(error, response, isLoading, makeRequest, axios) => {
          if(error) {
            return (<div>Something bad happened: {error.message} <button onClick={() => makeRequest({ params: { reload: true } })}>Retry</button></div>)
          }
          else if(isLoading) {
            return (
              <div>
               <CircularProgress />             
              </div>)
          }
          else if(response !== null) {
            return (
              <div>
                <Result data={response.data} refetch={makeRequest} setQueryValue={setQueryValue} setSearchValueMode={setSearchValueMode}/>
              </div>)
          }
          return (<div>Default message before request is made.</div>)
        }}
      </Get>
    </div>
  );
}

export default App;
