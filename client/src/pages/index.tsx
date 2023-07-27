import Head from 'next/head'
import {useEffect, useState} from 'react'
import axios from "axios"

export default function Home() {
    type result = {
        message: string;
    };
    type GetResponse = {
        data: result[];
    };

    let endPoint = 'http://127.0.0.1:8000/openai';
    const [post, setPost] = useState("Loading");
    useEffect(()=>{
        axios.get(endPoint).then((response) => {
            setPost(response.data.message);
        });
    }, []);

    return (
    <>
      <Head>
        <title>PokeDex</title>
        <meta name="description" content="PokeDex App run by openAi" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <div>{post}</div>
      </main>
    </>
  )
}
