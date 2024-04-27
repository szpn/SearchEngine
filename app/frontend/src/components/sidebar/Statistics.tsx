import React, { useState } from 'react';
import SideBarComponent from './SideBarComponent';
import './Statistics.css';
// @ts-ignore
import { ReactComponent as StatisticsIcon } from "../../assets/statistics-icon.svg";

export interface SearchStatisticsData {
    creation_time: number;
    search_time: number;
}

const Statistics: React.FC<{ data: SearchStatisticsData }> = ({data}) => {
    return (
        <SideBarComponent
            title={"Statistics"}
            Icon={StatisticsIcon}
            content={
                <>
                    <div className="statistics-section" id="general-statistics">
                        <div className="statistic-item">
                            <span className="statistic-label">Dictionary size:</span>
                            <span className="statistic-value">1000</span>
                        </div>
                        <div className="statistic-item">
                            <span className="statistic-label">Articles count</span>
                            <span className="statistic-value">50000</span>
                        </div>
                    </div>
                    <div className="statistics-section" id="time-statistics">
                        <div className="statistic-item">
                            <span className="statistic-label">Query time:</span>
                            <span className="statistic-value">{data.search_time.toPrecision(3)}</span>
                        </div>
                        <div className="statistic-item">
                            <span className="statistic-label">Description fetch time:</span>
                            <span className="statistic-value">{data.creation_time.toPrecision(3)}</span>
                        </div>
                    </div>
                </>
            }
        />
    );
};

export default Statistics;
