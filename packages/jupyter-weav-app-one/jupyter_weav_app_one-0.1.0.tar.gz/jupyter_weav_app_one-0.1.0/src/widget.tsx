
import { ReactWidget } from '@jupyterlab/apputils';

import React  from 'react';

/**
 * React component for a counter.
 *
 * @returns The React component
 */
const CounterComponent = (): JSX.Element => {
  return (
    <div style={{textAlign: "center"}}>
      <h1 style={{color:"blue"}}>Welcome to WEAV AI</h1> 
      <a href = "https://weav.ai/" target="_blank" title="weav homepage">
          <img height="100" width="100" src="https://img1.wsimg.com/isteam/ip/5944b92b-9cdf-4e95-9400-d95080c03bdb/Weav%20Logo%20-%200.6.png/:/rs=h:640/ll" alt="weav homepage" />
      </a>
    </div>
  );
};

/**
 * A Counter Lumino Widget that wraps a CounterComponent.
 */
export class CounterWidget extends ReactWidget {
  /**
   * Constructs a new CounterWidget.
   */
  constructor() {
    super();
    this.addClass('jp-ReactWidget');
  }

  render(): JSX.Element {
    return <CounterComponent />;
  }
}