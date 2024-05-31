// pages/index.js

import React from 'react';
import Head from 'next/head';

const Home = () => {
  return (
    <div>
      <Head>
        <title>WebSocket Demo</title>
      </Head>
      <iframe src="/web.html" style={{ width: '100%', height: '500px', border: 'none' }} />
    </div>
  );
};

export default Home;
