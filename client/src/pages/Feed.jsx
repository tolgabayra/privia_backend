import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useDisclosure, useToast } from '@chakra-ui/react'
import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
    Button
} from '@chakra-ui/react'
import { useDispatch } from "react-redux"
import { logout } from '../features/authSlice';
import { useState } from 'react'
import { useEffect } from 'react'
import { appAxios } from '../utils/appAxios'

export default function Feed() {

    const [topics, setTopics] = useState([])


    const { isOpen, onOpen, onClose } = useDisclosure()
    const navigate = useNavigate()
    const toast = useToast()
    const dispatch = useDispatch()



    useEffect(() => {
      appAxios.get("/api/v1/topic",{withCredentials: true})
      .then((res) => {
        console.log(res);
      })
      .catch(err=>console.log(err))
    },[])










    const submitLogout = () => {
        toast({
            title: 'Log out is successfull',
            status: 'success',
            duration: 3000,
            isClosable: true,
          })
      localStorage.clear()
      setTimeout(() => {
        
        navigate("/login")
        dispatch(logout())

      },2000)


    }





    return (
        <div>

            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>Create Topic</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                        dasdas
                    </ModalBody>

                    <ModalFooter>
                        <Button colorScheme='blue' mr={3} onClick={onClose}>
                            Close
                        </Button>
                        <Button variant='ghost'>Create</Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>

            <div className="flex justify-center w-screen h-screen px-4 text-gray-700">
                <div className="flex w-full max-w-screen-lg">
                    <div class="flex flex-col w-52 py-4 pr-3 bg-slate-100">
                        <Link className='px-3 py-2 mt-2 text-lg font-medium rounded-sm hover:bg-green-300' to="/profile">Profile</Link>

                        <button onClick={submitLogout} className='px-3 py-2 mt-2 text-lg font-medium rounded-sm border border-red-500 hover:bg-red-600 hover:text-white'>Logout</button>

                        <a class="flex px-3 py-2 mt-2 text-lg rounded-sm font-medium hover:bg-green-200 cursor-pointer">
                            <span class="flex-shrink-0 w-10 h-10 bg-green-400 rounded-full"></span>
                            <div class="flex flex-col ml-2">
                                <span class="mt-1 text-sm font-semibold leading-none">dasdas</span>
                                <span class="mt-1 text-xs leading-none">dasdas</span>
                            </div>
                        </a>
                    </div>

                    <div className="flex flex-col flex-grow border-l border-r border-gray-300">
                        <div className="flex justify-between flex-shrink-0 px-8 py-4 border-b border-gray-300">
                            <h1 className="text-xl font-semibold">Questions</h1>
                            <button onClick={onOpen}  className="flex items-center h-8 px-2 text-sm bg-green-300 rounded-lg hover:bg-green-200">Create Topic</button>
                        </div>




                       




                        <div className="flex-grow h-0 overflow-auto">
                            <div className="bg-green-50 shadow rounded-lg pb-4">
                                <div className="flex flex-row px-2 py-3 mx-3">
                                    <div className="w-auto h-auto rounded-full border-2 border-green-500">
                                        <img className="w-12 h-12 object-cover rounded-sm shadow cursor-pointer" alt="avatar" src="" />
                                    </div>
                                    <div className="flex flex-col mb-2 ml-4 mt-1">
                                        <div className="flex text-gray-600 text-sm font-semibold"><span className="flex-1 flex-shrink-0">tolga</span>
                                            <span className="mx-1 flex-1 flex-shrink-0"></span></div>
                                        <div className="flex w-full mt-1">
                                            <div className="text-blue-700 font-base text-xs mr-1 cursor-pointer">
                                                User: Tolga
                                            </div>
                                            <div className="text-gray-400 font-thin text-xs">
                                                •-POst Info
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div className="border-b border-gray-100 p-4"></div>

                                <div className="text-gray-600 font-semibold  mb-2 mx-3 px-2">title</div>
                                <div className="text-gray-500 text-sm mb-6 mx-3 px-2"> text</div>
                                <div className="flex justify-start mb-4 border-t border-gray-100">

                                    <div className="flex justify-end w-full mt-1 pt-2 pr-5">
                                        <span className="transition ease-out duration-300 hover:bg-blue-50 bg-blue-100 w-8 h-8 px-2 py-2 text-center rounded-full text-blue-400 cursor-pointer mr-2">
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" width="14px" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"></path>
                                            </svg>
                                        </span>
                                        <span className="transition ease-out duration-300 hover:bg-gray-50 bg-gray-100 h-8 px-2 py-2 text-center rounded-full text-gray-100 cursor-pointer">

                                        </span>
                                    </div>
                                </div>
                                <div className="flex w-full border-t border-gray-100">
                                    <div className="mt-3 mx-5 flex flex-row text-xs">
                                        <div className="flex text-gray-700 font-normal rounded-md mb-2 mr-4 items-center">Comments:<div className="ml-1 text-gray-400 text-ms"> 30</div></div>
                                        <div className="flex text-gray-700 font-normal rounded-md mb-2 mr-4 items-center">Views: <div className="ml-1 text-gray-400 text-ms"> 60k</div></div>
                                    </div>
                                    <div className="mt-3 mx-5 w-full flex justify-end text-xs">
                                        <div className="flex text-gray-700  rounded-md mb-2 mr-4 items-center">Likes: <div className="ml-1 text-gray-400 text-ms"> 120k</div></div>
                                    </div>
                                </div>
                                <div className="relative flex items-center self-center w-full max-w-xl p-4 overflow-hidden text-gray-600 focus-within:text-gray-400">
                                    <img className="w-10 h-10 object-cover rounded-full shadow mr-2 cursor-pointer" alt="User avatar" src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;ixlib=rb-1.2.1&amp;auto=format&amp;fit=crop&amp;w=2000&amp;q=80" />
                                    <span className="absolute inset-y-0 right-0 flex items-center pr-6">
                                        <button type="submit" className="p-1 focus:outline-none focus:shadow-none hover:text-blue-500">

                                            Yorum Yap
                                        </button>
                                    </span>
                                    <input type="text   " className="w-full py-2 pl-4 pr-10 text-sm bg-gray-100 border border-transparent appearance-none rounded-tg placeholder-gray-400 focus:bg-white focus:outline-none focus:border-blue-500 focus:text-gray-900 focus:shadow-outline-blue" placeholder="Post a comment..." autocomplete="off" />
                                </div>
                            </div>
                        </div>





                    </div>
                    <div className="flex flex-col flex-shrink-0 w-1/6 py-4 pl-5">
                        Trends
                    </div>
                </div>
            </div>


            

        </div>
    )
}
