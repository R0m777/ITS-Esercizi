import React from 'react'

const Clock = (props) => {
    console.log(props.timezone,props.country)
    const t=Date.now()+3600*props.timezone*1000;
    const data=new Date(t);
    return (
    <div>In {props.country} sono le{data.toLocaleDateString()} del giorno {data.toLocaleTimeString()}</div>
  )
}

export default Clock