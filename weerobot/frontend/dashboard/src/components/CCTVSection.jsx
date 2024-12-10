import React from 'react';
import { Box, Paper, Typography } from '@mui/material';

function CCTVSection() {
  console.log('CCTVSection rendered'); // 디버깅용 로그

  return (
    <Box sx={{ flex: 1, mr: 2 }}>
      <Paper elevation={3} sx={{ height: '100%', p: 2 }}>
        <Typography variant="h6" gutterBottom>
          CCTV Monitoring
        </Typography>
        <Box
          sx={{
            width: '100%',
            height: 'calc(100% - 40px)',
            bgcolor: 'black',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <Typography color="white">
            Waiting for CCTV stream...
          </Typography>
        </Box>
      </Paper>
    </Box>
  );
}

export default CCTVSection;