import { create } from 'zustand';  // 수정된 부분

export const useStore = create((set) => ({
  videoModalOpen: false,
  currentVideo: null,
  setVideoModalOpen: (isOpen) => set({ videoModalOpen: isOpen }),
  setCurrentVideo: (video) => set({ currentVideo: video }),
}));