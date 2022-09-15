import './components.css'
const Notification = ({message}) => {
    if(message === null) {
        return null
    }
    else {
        return ( 
            <div className="container">
            <div className="rectangle">
                <div className="notification-text">
                    <i className="material-icons">info</i>
                    <span>&nbsp;&nbsp;{message}</span>
                </div>
            </div>
        </div>
         );
    }
}
 
export default Notification;