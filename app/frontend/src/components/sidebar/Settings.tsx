import React, { useState } from 'react';
import SideBarComponent from './SideBarComponent';
// @ts-ignore
import { ReactComponent as SettingsIcon } from "../../assets/settings-icon.svg";
import './Settings.css';


interface SettingsProps {

    onUpdateSettings: (newSettings: {
        useSVD: boolean;
        maxResults: number
    }) => void;

    settings: {
        useSVD: boolean;
        maxResults: number
    };
}


const Settings: React.FC<SettingsProps> = ({onUpdateSettings, settings}) => {
    const [useSVD, setUseSVD] = useState(settings.useSVD);
    const [maxResults, setMaxResults] = useState(settings.maxResults);

    const handleSave = () => {
        const newSettings = { useSVD, maxResults };
        onUpdateSettings(newSettings);
    };

    return (
        <SideBarComponent
            title="Settings"
            Icon={SettingsIcon}
            content={
                <>
                    <div className="setting">
                        <label>Use SVD</label>
                        <input type="checkbox" checked={useSVD} onChange={() => setUseSVD(!useSVD)} />
                    </div>
                    <div className="setting">
                        <label>Max results</label>
                        <input type="number" min="1" value={maxResults} onChange={(e) => setMaxResults(parseInt(e.target.value))} />
                    </div>
                </>
            }
            onSave={handleSave}
        />
    );
};

export default Settings;
