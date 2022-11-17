import React from 'react'
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import Button from '@mui/material/Button';
import { saveAs } from "file-saver";
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

export const Output = (props) => {

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

      const b64toBlob = (b64Data, contentType='', sliceSize=512) => {
        const byteCharacters = atob(b64Data);
        const byteArrays = [];
      
        for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
          const slice = byteCharacters.slice(offset, offset + sliceSize);
      
          const byteNumbers = new Array(slice.length);
          for (let i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
          }
      
          const byteArray = new Uint8Array(byteNumbers);
          byteArrays.push(byteArray);
        }
      
        const blob = new Blob(byteArrays, {type: contentType});
        return blob;
      }

      const Download = () => {
        for (let i = 0; i < props.resultImages.length; i++) {
          console.log(props.resultImages[i]);
          const blob = b64toBlob(props.resultImages[i], 'image/png');
          saveAs(blob, `image${i}.png`);
        }
      };


  return (
    <>
    <div style={someStyle}>
    <div style={{ marginTop: '2%', display: 'flex', justifyContent: 'center' }}>
          <ImageList sx={{ width: 700, height: 450, borderRadius: '3%' }} cols={4} rowHeight={164}>
            {props.resultImages.map((item) => (
              <ImageListItem>
                <img
                src = {`data:image/png;base64,${item}`}
                  style={{ borderRadius: '8%' }}
                />
              </ImageListItem>
            ))}
          </ImageList>
        </div>

        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '2%' }}>
          <Button variant="contained" size="large" onClick={Download} style={{ backgroundColor: "rgba(82, 82, 82, 0.5)", width: '14em' }}> Download </Button>
        </div>
    </div>
    </>
  )
}
