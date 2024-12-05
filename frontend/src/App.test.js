import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

test('renders document upload area', () => {
  render(<App />);
  expect(screen.getByText(/drag and drop a pdf file here/i)).toBeInTheDocument();
});

test('shows placeholder when no documents are uploaded', () => {
  render(<App />);
  expect(screen.getByText(/select or upload a document to start a conversation/i)).toBeInTheDocument();
});

test('api key change button exists', () => {
  render(<App />);
  expect(screen.getByText(/change/i)).toBeInTheDocument();
});