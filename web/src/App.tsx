import {useEffect, useState} from 'react';
import './App.css';
import Observation from './types/Observation';
import Site from './types/Site';

type DataRow = Site & {
    observations: Observation[]
};

function App() {
    const [siteData, setSiteData] = useState<DataRow[]>([]);

    useEffect(() => {
        // TODO: Fetch sites
    }, [])

    return (
        <div className="App">
            <header className="App-header">
                <h1>
                    Welcome to LogJam v0.1
                </h1>
                <p>
                    View current flows below!
                </p>
            </header>

            <div>
                {siteData.map((site) => {
                    return (
                        <ul>
                            {site.observations.map(
                                (obs) => <li> {`${obs.timestamp}:  ${obs.value}`}</li>
                            )}
                        </ul>
                    )
                })}

            </div>
        </div>
    );
}

export default App;
