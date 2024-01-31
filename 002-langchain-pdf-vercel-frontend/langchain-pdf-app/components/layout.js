import styles from '../styles/layout.module.css'

export default function Layout(props) {
  return (
    <div className={styles.layout}>
      <h1 className={styles.title}>Basic PDF CRUD App</h1>
      <p className={styles.subtitle}>By <a href="https://aiaccelera.com/" target="_blank">AI Accelera</a> and <a href="https://aceleradoraai.com/" target="_blank">Aceleradora AI</a></p>
      {props.children}
    </div>
  )
}