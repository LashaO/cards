import logo from "./logo.svg";
import "./App.css";
import "./index.scss";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faAngleRight } from "@fortawesome/free-solid-svg-icons";

function App() {
  const Continue = () => {
    function handleClick(e) {
      e.preventDefault();
      console.log("The link was clicked.");
    }

    return (
      <div className="continue">
        <button onClick={handleClick}>
          Continue
          <FontAwesomeIcon className="icon" icon={faAngleRight} />
        </button>
      </div>
    );
  };

  return (
    <div>
      {" "}
      <div className="pricing-table">
        <div className="alpha">
          <div className="price">
            <span>$</span>2
          </div>
          <h2>Individual</h2>
          <div className="feature">
            <h3>
              Office <span>20gb</span>
              <div className="progress one"></div>
            </h3>
          </div>
          <div className="feature">
            <h3>
              Home <span>10gb</span>
              <div className="progress two"></div>
            </h3>
          </div>
          <Continue />
        </div>

        <div className="beta">
          <div className="price">
            <span>$</span>5
          </div>
          <h2>Shared</h2>
          <div className="large-feature">
            <p>Family</p>
            <h3>100 GB</h3>
          </div>
          <Continue />
        </div>
        <p>sometext</p>

        <div className="omega">
          <h2>Unlimited</h2>
        </div>
      </div>
    </div>
  );
}

export default App;
