import React from 'react'
import {useEffect} from 'react';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import Button from '@mui/material/Button';

export const Preview = (props) => {

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

  // const itemData = [
  //   {
  //     img: 'https://images.unsplash.com/photo-1551963831-b3b1ca40c98e',
  //     title: 'Breakfast',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1551782450-a2132b4ba21d',
  //     title: 'Burger',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1522770179533-24471fcdba45',
  //     title: 'Camera',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1444418776041-9c7e33cc5a9c',
  //     title: 'Coffee',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1533827432537-70133748f5c8',
  //     title: 'Hats',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1558642452-9d2a7deb7f62',
  //     title: 'Honey',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1516802273409-68526ee1bdd6',
  //     title: 'Basketball',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1518756131217-31eb79b20e8f',
  //     title: 'Fern',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1597645587822-e99fa5d45d25',
  //     title: 'Mushrooms',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1567306301408-9b74779a11af',
  //     title: 'Tomato basil',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1471357674240-e1a485acb3e1',
  //     title: 'Sea star',
  //   },
  //   {
  //     img: 'https://images.unsplash.com/photo-1589118949245-7d38baf380d6',
  //     title: 'Bike',
  //   },
  // ];

  const [ImageData, setImageData] = React.useState([]);

  useEffect(() => {
    const objList = [];
    for(let i = 0; i < props.imgArray.length; i++)
    {
      objList.push({
        img: props.imgArray[i],
        title: i.toString()
      })
    }
    setImageData(objList);
  },[props.imgArray]);
  
  

  const Proceed = () => {
    console.log("Proceed");
  }

  return (
    <>
      <div style={someStyle}>
        <div style={{ marginTop: '2%', display: 'flex', justifyContent: 'center' }}>
          <ImageList sx={{ width: 700, height: 450, borderRadius: '3%' }} cols={4} rowHeight={164}>
            {ImageData.map((item) => (
              <ImageListItem key={item.img}>
                <img
                  src={`${item.img}?w=164&h=164&fit=crop&auto=format`}
                  srcSet={`${item.img}?w=164&h=164&fit=crop&auto=format&dpr=2 2x`}
                  alt={item.title}
                  // loading="lazy"
                  style={{ borderRadius: '8%' }}
                />
              </ImageListItem>
            ))}
          </ImageList>
        </div>

        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '2%' }}>
          <Button variant="contained" size="large" onClick={Proceed} style={{ backgroundColor: "rgba(82, 82, 82, 0.5)", width: '14em' }}> Proceed </Button>
        </div>

      </div>
    </>
  )
}
