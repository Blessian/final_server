import { useEffect, useRef } from 'react';
import io from 'socket.io-client';
import { useStore } from './useStore';

export const useSocket = () => {
  const socketRef = useRef(null);
  const { setVideoModalOpen, setCurrentVideo } = useStore();

  useEffect(() => {
    socketRef.current = io('http://127.0.0.1:8000');

    socketRef.current.on('connect', () => {
      console.log('Socket connected');
    });

    socketRef.current.on('video_stream', (data) => {
      setCurrentVideo(data);
      setVideoModalOpen(true);
    });

    return () => {
      if (socketRef.current) {
        socketRef.current.disconnect();
      }
    };
  }, []);

  return socketRef.current;
};