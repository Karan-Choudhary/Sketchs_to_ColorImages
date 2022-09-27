import React from 'react'

export const Loading = () => {

    let someStyle = {
        // minHeight: '85vh',
        position: 'fixed',
        minHeight: '100%',
        minWidth: '100%',
        color: 'black',
        backgroundImage: "url(/img/bg.png)",
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
      };

  return (
    <>
    <div style={someStyle}>
        <div style={{display: 'flex', justifyContent: 'center', alignItems:'center'}}>
            <p style={{ color: 'white', fontSize: '2.375em', fontFamily: 'Inter', fontStyle: 'Normal'}}> Please wait<br/> Processing... </p>
        </div>
    </div>
    </>
  )
}
