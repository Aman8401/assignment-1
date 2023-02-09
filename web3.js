import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { fetch as fetchPolyfill } from 'whatwg-fetch';

function App() {
  const [blockData, setBlockData] = useState({});
  const [transactionData, setTransactionData] = useState({});
  const [web3, setWeb3] = useState(null);

  useEffect() ; {
    async function initWeb3() {
      // Check if web3 is available
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        setWeb3(web3);
        try {
          // Request account access if needed
          await window.ethereum.enable();
        } catch (error) {
          console.error(error);
        }
      } else if (window.web3) {
        const web3 = new Web3(window.web3.currentProvider);
        setWeb3(web3);
      }}}}
