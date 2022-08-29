const StatisticsLine = (props) => {
    return (
        <tr>
            <td>{props.text}</td>
            <td>{props.value}</td>
        </tr>
    )
}


const Statistics = (props) => {
    const {good, bad, neutral} = props
    if(good || bad || neutral) {
        return (
            <div>
                <h1>Statistics</h1>
                <table>
                <tbody>
                <StatisticsLine text = "Good" value = {good} />
                <StatisticsLine text = "Bad" value = {bad} />
                <StatisticsLine text = "Neutral" value = {neutral} />
                <StatisticsLine text = "All" value = {good+bad+neutral} />
                <StatisticsLine text = "Average" value = {(good+bad+neutral)/3} />
                <StatisticsLine text = "Percentage" value = {good/(good+bad+neutral)} />
                </tbody>
                </table>
            </div>
          )
    }
    else {
        return (
            <div>No Feedback Given</div>
        )
    }
    
}
 
export default Statistics;