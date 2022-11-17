import React from 'react'
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import { useRef } from 'react';
import { useNavigate } from 'react-router-dom';

export const MainContent = (props) => {

  let someStyle = {
    // minHeight: '85vh',
    position: 'absolute',
    minHeight: '100%',
    minWidth: '100%',
    color: 'black',
    backgroundImage: "url(/img/bg.png)",
    backgroundRepeat: 'no-repeat',
    backgroundSize: 'cover',
  };

  const [SliderValue, setSliderValue] = React.useState(8);
  // const [ImagesNames, setImagesNames] = React.useState([]);

  const ImageSlider = styled(Slider)({
    color: '#FFFFFF',
    width: '100%',
    height: 15,
    '& .MuiSlider-track': {
      border: 'none',
    },
    '& .MuiSlider-thumb': {
      height: 30,
      width: 30,
      backgroundColor: '#fffff',
      border: '2px solid currentColor',
      '&:focus, &:hover, &.Mui-active, &.Mui-focusVisible': {
        boxShadow: 'inherit',
      },
      '&:before': {
        display: 'none',
      },
    },
    '& .MuiSlider-valueLabel': {
      lineHeight: 1.2,
      fontSize: 12,
      background: 'unset',
      padding: 0,
      width: 42,
      height: 42,
      borderRadius: '50% 50% 50% 50%',
      backgroundColor: '#000000',
      transformOrigin: 'bottom left',
      transform: 'translate(50%, -100%) rotate(-45deg) scale(0)',
      '&:before': { display: 'none' },
      '&.MuiSlider-valueLabelOpen': {
        transform: 'translate(50%, -100%) rotate(-45deg) scale(1)',
      },
      '& > *': {
        transform: 'rotate(45deg)',
      },
    },
  });


  const inputRef = useRef(null);

  const BrowseImage = () => {
    inputRef.current.click();
  };

  let navigate  = useNavigate();

  const Proceed = () => {
        navigate('/Preview');
  };

  const handleFileChange = event => {
    let fileArray = event.target.files;
    props.setImagesNames(fileArray);
  };

  return (
    <>
      <div className='container' style={someStyle}>
        <div style={{ marginLeft: '7%', marginRight: '7%' }}>
          <Grid style={{ paddingTop: '1.92%', paddingBottom: '2%' }} container spacing={1} columns={4}>
            <Grid item xs={2.5}>
              <p style={{ color: 'white', fontSize: '4.375em', fontFamily: 'Inter', fontStyle: 'Normal' }}>Paint<br></br> The Collection</p>
            </Grid>
            <Grid item xs={1.5}>
              <p style={{ color: 'white', fontSize: '1.5625em', fontFamily: 'Inter', fontStyle: 'Normal', paddingTop: '10%' }}>New way to paint your collection. Find out more about on going improvement.</p>
            </Grid>
          </Grid>

          <Box >
            <Box sx={{ m: 3 }} />
            <Typography gutterBottom style={{ color: 'white', fontSize: '2.4375em', fontFamily: 'Inter', fontStyle: 'Normal' }}>Tell us the number of images</Typography>
            <ImageSlider
              valueLabelDisplay="auto"
              // aria-label="pretto slider"
              disableSwap={false}
              defaultValue={SliderValue}
              // components = {{Thumb: Preview}}
              // write onChange function
              onChange={(event, newValue) => {
                setSliderValue(newValue);
                console.log(newValue);
              }}
            />
          </Box>

          <Grid style={{ paddingTop: '6.92%' }} container spacing={0} columns={10}>
            <Grid item xs={5}>
              <input style={{ display: 'none' }} ref={inputRef} type="file" onChange={handleFileChange} multiple />
              <Button variant="contained" size="large" onClick={BrowseImage} style={{ backgroundColor: "rgba(82, 82, 82, 0.5)", width: '14em', marginLeft: '50%' }}> Browse Images </Button>
            </Grid>
            <Grid item xs={5}>
              <Button variant="contained" size="large" onClick={Proceed} style={{ backgroundColor: "rgba(82, 82, 82, 0.5)", width: '14em' }}> Proceed </Button>
            </Grid>
          </Grid>
        </div>
      </div>

    </>
  );
}
