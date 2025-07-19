<?php
namespace App\Controller;

use App\Service\OpenAiService;

class ChatController
{
    private OpenAiService $service;

    public function __construct(OpenAiService $service)
    {
        $this->service = $service;
    }

    public function handle(): void
    {
        $question = trim($_POST['question'] ?? '');
        $answer   = '';

        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            if ($question === '') {
                $answer = 'Please enter a question.';
            } else {
                try {
                    $answer = $this->service->ask($question);
                } catch (\Exception $e) {
                    $answer = 'Error: ' . $e->getMessage();
                }
            }
        }

        include __DIR__ . '/../../templates/chat.php';
    }
}
