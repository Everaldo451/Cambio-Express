const feedBacks:FeedBack[] = [
    {date: new Date(),first_name: 'AnyName',comment: 'Test comment'},
    {date: new Date(),first_name: 'OtherName',comment: 'Other test comment'},
];

jest.mock('@/components/home/FeedBacks', () => {
    const originalModule = jest.requireActual('@/components/home/FeedBacks')

    return {
        __esModule: true,
        ...originalModule,
        getFeedBacks: jest.fn(() => feedBacks)
    }
})
import FeedBacks, { FeedBack } from '@/components/home/FeedBacks';
import { render, screen } from '@testing-library/react';

describe('Feedbacks in home page', () => {
    beforeEach(() => {
        window.HTMLElement.prototype.scrollIntoView = jest.fn();
    });

    test('feedbacks must appear', async () => {
        render(<FeedBacks/>)
        for (const value of feedBacks) {
            const feedbackComment = await screen.findByText(value.comment)
            expect(feedbackComment).toBeDefined()
            console.log(`Feedback with comment "${value.comment}" exists.`)
            const feedbackUserName = await screen.findByText(value.first_name)
            expect(feedbackUserName).toBeDefined()
            console.log(`Feedback with user "${value.comment}" exists.`)
        }
    });
})