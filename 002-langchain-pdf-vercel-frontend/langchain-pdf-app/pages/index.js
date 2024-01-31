import Head from 'next/head'
import Layout from '../components/layout';
import PDFList from '../components/pdf-list';
import styles from '../styles/layout.module.css'

export default function Home() {
  return (
    <div>
      <Head>
        <title>Basic PDF CRUD App</title>
        <meta name="description" content="Basic PDF CRUD App" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Layout>
        <PDFList />
      </Layout>
    </div>
  )
}