
import { ReactWidget } from '@jupyterlab/apputils';

import React  from 'react';

import LandingPage from './components/LandingPage/LandingPage';


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
    return (
    <div style={{textAlign: "center"}}>
      <LandingPage></LandingPage>
    </div>
    )
  }
}