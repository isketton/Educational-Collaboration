import React, { useState } from "react";
import {
  useQuery,
  useMutation,
  useQueryClient,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'

// button to generate report card based on current grades, then will display
export default function ReportCard() {
  
}

// Temp func to fetch user data, fetch user data based on token 
async function fetchUser(email, password) {
  const response = await fetch('/user/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json'},
    body: JSON.stringify({email, password}),
  });
  
  if (!response.ok) {
    throw new Error('Login failed');
  }

  return await response.json();

  
}