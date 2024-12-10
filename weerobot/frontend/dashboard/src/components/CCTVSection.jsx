import React, { useEffect, useState, useRef } from 'react';
import { Box, Paper, Typography } from '@mui/material';

function CCTVSection() {
  const [isConnected, setIsConnected] = useState(false);
  const imageRef = useRef(null);
  const wsRef = useRef(null);

  useEffect(() => {
    // WebSocket 연결
    wsRef.current = new WebSocket('ws://localhost:1221');
    const ws = wsRef.current;

    ws.onopen = () => {
      console.log('Connected to video server');
      setIsConnected(true);
    };

    ws.onmessage = (event) => {
      // base64 이미지 데이터를 직접 img 태그의 src에 설정
      if (imageRef.current) {
        imageRef.current.src = `data:image/jpeg;base64,${event.data}`;
      }
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      setIsConnected(false);
    };

    ws.onclose = () => {
      console.log('Disconnected from video server');
      setIsConnected(false);
    };

    // 컴포넌트 언마운트 시 연결 종료
    return () => {
      if (ws.readyState === WebSocket.OPEN) {
        ws.close();
      }
    };
  }, []);

  return (
    <Box sx={{ flex: 1, mr: 2 }}>
      <Paper elevation={3} sx={{ height: '100%', p: 2 }}>
        <Typography variant="h6" gutterBottom>
          CCTV Monitoring
          {isConnected && (
            <Box
              component="span"
              sx={{
                display: 'inline-block',
                width: 10,
                height: 10,
                borderRadius: '50%',
                bgcolor: 'success.main',
                ml: 2
              }}
            />
          )}
        </Typography>
        <Box
          sx={{
            width: '100%',
            height: 'calc(100% - 40px)',
            bgcolor: 'black',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            overflow: 'hidden',
          }}
        >
          {!isConnected ? (
            <Typography color="white">
              Connecting to video stream...
            </Typography>
          ) : (
            <img
              ref={imageRef}
              alt="CCTV Stream"
              style={{
                width: '100%',
                height: '100%',
                objectFit: 'contain'
              }}
            />
          )}
        </Box>
      </Paper>
    </Box>
  );
}

export default CCTVSection;