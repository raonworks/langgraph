import viteLogo from "./assets/vite.svg";
import heroImg from "./assets/hero.png";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  const handleOnClick = () => {
    //test 라는 로그를 찍어줘
    alert("hello");
  };

  const sumAll = (a: number, b: number): number => {
  }