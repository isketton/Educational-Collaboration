import React, { useState } from "react";
import {
  useQuery,
  useMutation,
  useQueryClient,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import Cookies from 'js-cookie';
import axios from "axios";


export default function Grades() {




  const {data, isLoading, error} = useQuery({
    queryKey: ['grades'], 
    queryFn: async () => {
      // check if authtoken is null, if so in backend return 404
      return axios.get('http://localhost:8001/schoolapp/reports/1/', {withCredentials: true});
    }
  });



  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>An error has occurred: {error.message}</div>;
  }
 
  return (
    <div className="box">
       <li> {data.data.grades} </li>
    </div>
  )
}