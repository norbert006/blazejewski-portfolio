import Navbar from './components/Navbar'
import { Route, Routes } from "react-router-dom"

function App() {
  return (
    <div>
      <Navbar />
        <Routes>
          <Route path='/'> </Route>
        </Routes>
    </div>
  );
}

export default App;
