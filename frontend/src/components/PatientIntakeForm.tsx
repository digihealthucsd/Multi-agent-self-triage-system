import { useState } from 'react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Label } from './ui/label';
import { RadioGroup, RadioGroupItem } from './ui/radio-group';
import { PatientInfo } from '../App';

interface PatientIntakeFormProps {
  onSubmit: (info: PatientInfo) => void;
  queryingFor: 'myself' | 'someone-else';
}

export function PatientIntakeForm({ onSubmit, queryingFor }: PatientIntakeFormProps) {
  const [name, setName] = useState('');
  const [sex, setSex] = useState('');
  const [age, setAge] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({ 
      name, 
      sex, 
      age, 
      isForSomeoneElse: queryingFor === 'someone-else' 
    });
  };

  const isForSomeoneElse = queryingFor === 'someone-else';

  return (
    <div className="bg-white rounded-3xl shadow-xl shadow-blue-100/50 p-8 md:p-12 border border-gray-100">
      <form onSubmit={handleSubmit} className="space-y-8">
        {/* Name Field */}
        <div className="space-y-3">
          <Label htmlFor="name" className="text-gray-700">
            {isForSomeoneElse ? 'Please enter your name' : 'Please enter your name'}
          </Label>
          <Input
            id="name"
            type="text"
            placeholder={isForSomeoneElse ? 'Your full name' : 'Enter your full name'}
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            className="h-12 border-gray-200 focus:border-blue-400 focus:ring-blue-400/20 rounded-xl"
          />
        </div>

        {/* Sex Field */}
        <div className="space-y-3">
          <Label className="text-gray-700">
            {isForSomeoneElse ? 'Please select their sex' : 'Please select your sex'}
          </Label>
          <RadioGroup value={sex} onValueChange={setSex} className="flex flex-col sm:flex-row gap-3">
            <div className="flex-1">
              <div className="relative">
                <RadioGroupItem
                  value="female"
                  id="female"
                  className="peer sr-only"
                />
                <Label
                  htmlFor="female"
                  className="flex items-center justify-center h-12 px-6 rounded-xl border-2 border-gray-200 cursor-pointer transition-all hover:border-blue-300 hover:bg-blue-50/50 peer-data-[state=checked]:border-blue-500 peer-data-[state=checked]:bg-blue-50 peer-data-[state=checked]:text-blue-700"
                >
                  Female
                </Label>
              </div>
            </div>
            <div className="flex-1">
              <div className="relative">
                <RadioGroupItem
                  value="male"
                  id="male"
                  className="peer sr-only"
                />
                <Label
                  htmlFor="male"
                  className="flex items-center justify-center h-12 px-6 rounded-xl border-2 border-gray-200 cursor-pointer transition-all hover:border-blue-300 hover:bg-blue-50/50 peer-data-[state=checked]:border-blue-500 peer-data-[state=checked]:bg-blue-50 peer-data-[state=checked]:text-blue-700"
                >
                  Male
                </Label>
              </div>
            </div>
            <div className="flex-1">
              <div className="relative">
                <RadioGroupItem
                  value="prefer-not-to-say"
                  id="prefer-not-to-say"
                  className="peer sr-only"
                />
                <Label
                  htmlFor="prefer-not-to-say"
                  className="flex items-center justify-center h-12 px-6 rounded-xl border-2 border-gray-200 cursor-pointer transition-all hover:border-blue-300 hover:bg-blue-50/50 peer-data-[state=checked]:border-blue-500 peer-data-[state=checked]:bg-blue-50 peer-data-[state=checked]:text-blue-700"
                >
                  Prefer not to say
                </Label>
              </div>
            </div>
          </RadioGroup>
        </div>

        {/* Age Field */}
        <div className="space-y-3">
          <Label htmlFor="age" className="text-gray-700">
            {isForSomeoneElse ? 'Please enter the age of the person you are querying for' : 'Please enter your age'}
          </Label>
          <Input
            id="age"
            type="number"
            placeholder={isForSomeoneElse ? 'Their age' : 'Enter your age'}
            value={age}
            onChange={(e) => setAge(e.target.value)}
            required
            min="0"
            max="150"
            className="h-12 border-gray-200 focus:border-blue-400 focus:ring-blue-400/20 rounded-xl"
          />
        </div>

        {/* Submit Button */}
        <Button
          type="submit"
          className="w-full h-14 bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white rounded-xl shadow-lg shadow-blue-200 transition-all duration-200 hover:shadow-xl"
        >
          Start Chat
        </Button>
      </form>
    </div>
  );
}
